from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import (
    Workout,
    WorkoutMuscle,
    WorkoutExercise,
    WorkoutSet
)
from app.schemas import WorkoutCreate

router = APIRouter(
    prefix="/workout",
    tags=["Workout"]
)

@router.post("/")
def save_workout(
    payload: WorkoutCreate,
    db: Session = Depends(get_db)
):
    workout = Workout(
        workout_date=payload.date,
        duration=payload.duration,
        workout_type=payload.type,
        notes=payload.notes
    )

    db.add(workout)
    db.commit()
    db.refresh(workout)

    for muscle in payload.muscles:
        db.add(
            WorkoutMuscle(
                workout_id=workout.id,
                muscle_name=muscle
            )
        )

    for ex in payload.exercises:

        exercise = WorkoutExercise(
            workout_id=workout.id,
            exercise_name=ex.name
        )

        db.add(exercise)
        db.commit()
        db.refresh(exercise)

        for st in ex.sets:
            db.add(
                WorkoutSet(
                    exercise_id=exercise.id,
                    weight=st.weight,
                    reps=st.reps
                )
            )

    db.commit()

    return {
        "message": "Workout saved",
        "id": workout.id
    }

@router.get("/")
def get_workouts(
    db: Session = Depends(get_db)
):
    workouts = db.query(Workout).all()

    result = []

    for workout in workouts:

        muscles = db.query(WorkoutMuscle).filter(
            WorkoutMuscle.workout_id == workout.id
        ).all()

        exercises = db.query(WorkoutExercise).filter(
            WorkoutExercise.workout_id == workout.id
        ).all()

        exercise_data = []

        for exercise in exercises:

            sets = db.query(WorkoutSet).filter(
                WorkoutSet.exercise_id == exercise.id
            ).all()

            exercise_data.append({
                "name": exercise.exercise_name,
                "sets": [
                    {
                        "weight": s.weight,
                        "reps": s.reps
                    }
                    for s in sets
                ]
            })

        result.append({
            "id": workout.id,
            "date": workout.workout_date,
            "duration": workout.duration,
            "type": workout.workout_type,
            "notes": workout.notes,
            "muscles": [
                m.muscle_name
                for m in muscles
            ],
            "exercises": exercise_data
        })

    return result


@router.delete("/{id}")
def delete_workout(
    id: int,
    db: Session = Depends(get_db)
):
    workout = db.query(Workout).filter(
        Workout.id == id
    ).first()

    if not workout:
        return {"message": "Workout not found"}

    db.delete(workout)
    db.commit()

    return {"message": "Deleted"}