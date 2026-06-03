from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models import CommunicationLog

from app.schemas import CommunicationCreate

router = APIRouter(
    prefix="/communication",
    tags=["Communication"]
);


@router.post("/")
def save_communication(
    payload: CommunicationCreate,
    db: Session = Depends(get_db)
):
    log = CommunicationLog(
        date=payload.date,
        activity=payload.activity,
        minutes=payload.minutes,
        video_title=payload.video_title,
        video_url=payload.video_url,
        creator=payload.creator,
        self_rating=payload.self_rating,
        summary=payload.summary,
        principle=payload.principle,
        technique=payload.technique,
        pronunciation=payload.pronunciation,
        topic_spoken=payload.topic_spoken,
        mistakes=payload.mistakes,
        corrections=payload.corrections
    )

    db.add(log)

    db.commit()

    db.refresh(log)

    print(payload)
    print(payload.model_dump())

    return log

@router.get("/")
def get_logs(
    db: Session = Depends(get_db)
):
    return db.query(
        CommunicationLog
    ).all()


@router.delete("/{id}")
def delete_log(
    id: int,
    db: Session = Depends(get_db)
):
    log = db.query(
        CommunicationLog
    ).filter(
        CommunicationLog.id == id
    ).first()

    if not log:
        return {
            "message": "Log not found"
        }

    db.delete(log)

    db.commit()

    return {
        "message": "Deleted successfully"
    }