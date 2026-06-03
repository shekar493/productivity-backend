from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import DSAProblem
from app.schemas import DSAProblemCreate

router = APIRouter(
    prefix="/dsa",
    tags=["DSA"]
)


@router.post("/")
def create_problem(
    payload: DSAProblemCreate,
    db: Session = Depends(get_db)
):
    problem = DSAProblem(**payload.model_dump())

    db.add(problem)
    db.commit()
    db.refresh(problem)

    return problem


@router.get("/")
def get_problems(
    db: Session = Depends(get_db)
):
    return db.query(DSAProblem).all()


@router.get("/{problem_id}")
def get_problem(
    problem_id: int,
    db: Session = Depends(get_db)
):
    return db.query(DSAProblem).filter(
        DSAProblem.id == problem_id
    ).first()


@router.delete("/{problem_id}")
def delete_problem(
    problem_id: int,
    db: Session = Depends(get_db)
):
    problem = db.query(DSAProblem).filter(
        DSAProblem.id == problem_id
    ).first()

    db.delete(problem)
    db.commit()

    return {"message": "Deleted"}