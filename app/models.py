from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Text
from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Text
)

from app.database import Base


class DSAProblem(Base):
    __tablename__ = "dsa_problems"

    id = Column(Integer, primary_key=True, index=True)

    problem_date = Column(Date)

    platform = Column(String(50))
    question_name = Column(String(255))
    question_link = Column(Text)

    difficulty = Column(String(20))
    topic = Column(String(100))
    pattern = Column(String(100))

    time_taken = Column(Integer)

    solved_status = Column(String(50))

    confidence = Column(Integer)

    learned = Column(Text)
    key_observation = Column(Text)
    important_trick = Column(Text)
    common_mistake = Column(Text)
    edge_cases = Column(Text)
    interview_relevance = Column(Text)

    articles = Column(Text)
    videos = Column(Text)

    revision_count = Column(Integer, default=0)

    
class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)

    workout_date = Column(Date)
    duration = Column(Integer)
    workout_type = Column(String(50))
    notes = Column(Text)

    muscles = relationship(
        "WorkoutMuscle",
        cascade="all, delete"
    )

    exercises = relationship(
        "WorkoutExercise",
        cascade="all, delete"
    )

class WorkoutMuscle(Base):
    __tablename__ = "workout_muscles"

    id = Column(Integer, primary_key=True)

    workout_id = Column(
        Integer,
        ForeignKey("workouts.id")
    )

    muscle_name = Column(String(100))

class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id = Column(Integer, primary_key=True)

    workout_id = Column(
        Integer,
        ForeignKey("workouts.id")
    )

    exercise_name = Column(String(255))

    sets = relationship(
        "WorkoutSet",
        cascade="all, delete"
    )

class WorkoutSet(Base):
    __tablename__ = "workout_sets"

    id = Column(Integer, primary_key=True)

    exercise_id = Column(
        Integer,
        ForeignKey("workout_exercises.id")
    )

    weight = Column(Float)

    reps = Column(Integer)

class CommunicationLog(Base):
    __tablename__ = "communication_logs"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(Date)

    activity = Column(String(100))

    minutes = Column(Integer)

    video_title = Column(String(255))
    video_url = Column(Text)
    creator = Column(String(255))

    self_rating = Column(Integer)

    summary = Column(Text)

    principle = Column(Text)

    technique = Column(Text)

    pronunciation = Column(Text)

    topic_spoken = Column(Text)

    mistakes = Column(Text)

    corrections = Column(Text)