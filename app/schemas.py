from pydantic import BaseModel
from datetime import date
from typing import Optional

from typing import List, Optional
from datetime import date
from pydantic import BaseModel, Field



class WorkoutSetCreate(BaseModel):
    weight: float
    reps: int


class WorkoutExerciseCreate(BaseModel):
    name: str
    sets: List[WorkoutSetCreate]


class WorkoutCreate(BaseModel):
    date: date
    duration: int
    type: str
    muscles: List[str]
    notes: Optional[str] = None
    exercises: List[WorkoutExerciseCreate]


class DSAProblemCreate(BaseModel):
    problem_date: date

    platform: str
    question_name: str
    question_link: Optional[str] = None

    difficulty: str
    topic: Optional[str] = None
    pattern: Optional[str] = None

    time_taken: int

    solved_status: str

    confidence: int

    learned: Optional[str] = None
    key_observation: Optional[str] = None
    important_trick: Optional[str] = None
    common_mistake: Optional[str] = None
    edge_cases: Optional[str] = None
    interview_relevance: Optional[str] = None

    articles: Optional[str] = None
    videos: Optional[str] = None


class DSAProblemResponse(DSAProblemCreate):
    id: int
    revision_count: int

    class Config:
        from_attributes = True



class WorkoutSetResponse(BaseModel):
    weight: float
    reps: int

    class Config:
        from_attributes = True


class WorkoutExerciseResponse(BaseModel):
    name: str
    sets: list[WorkoutSetResponse]


class WorkoutResponse(BaseModel):
    id: int
    date: date
    duration: int
    type: str
    notes: str | None
    muscles: list[str]
    exercises: list[WorkoutExerciseResponse]

class CommunicationCreate(BaseModel):
    date: date

    activity: str

    minutes: int

    video_title: Optional[str] = Field(None, alias="videoTitle")
    video_url: Optional[str] = Field(None, alias="videoUrl")
    creator: Optional[str] = None

    self_rating: Optional[int] = None

    summary: Optional[str] = None

    principle: Optional[str] = None

    technique: Optional[str] = None

    pronunciation: Optional[str] = None

    topic_spoken: Optional[str] = None

    mistakes: Optional[str] = None

    corrections: Optional[str] = None