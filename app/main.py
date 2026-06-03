from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.routers import workout
from app.database import engine, Base
from app import models
from app.routers import dsa
from app.routers import communication

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Productivity API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(dsa.router)

app.include_router(workout.router)

app.include_router(
    communication.router
)