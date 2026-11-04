from fastapi import FastAPI, HTTPException
from workout_logger import create_workout
from pydantic import BaseModel

# Describe the required fields and types for a new workout request.
class WorkoutCreate(BaseModel):
    date: str
    day_type: str
    duration_minutes: int
    energy: int

# Create the application that handles API requests.
app = FastAPI()

# Keep sample workouts in memory; changes are lost when the server restarts.
workouts = [
    {
        "id": 1,
        "date": "2026-11-03",
        "day_type": "PUSH",
        "duration_minutes": 80,
        "energy": 7,
        "exercises": [
            {"name": "Bench Press",
             "sets": 3
             },
            {"name": "Overhead Press",
             "sets": 2
             }
        ]
    },

    {
        "id": 2,
        "date": "2026-11-04",
        "day_type": "PULL",
        "duration_minutes": 75,
        "energy": 9,
        "exercises": [
            {"name": "Pull Up",
             "sets": 3
             },
            {"name": "Cable Row",
             "sets": 3
             }
        ]
    }
]

# Return a welcome message from the root endpoint.
@app.get("/")
def read_root():
    return {"message": "Welcome to my Workout Assistant Project"}

# Provide a simple way to check that the API is responding.
@app.get("/health")
def read_health():
    return {"status": "ok"}

# Return workouts with optional day type and minimum energy filters.
@app.get("/workouts")
def read_workouts(day_type: str | None = None, min_energy: int | None = None):

    # Return the full list when no filters are provided.
    if day_type is None and min_energy is None:
        return workouts
    
    matching_workouts = []

    for workout in workouts:
        # Skip workouts that do not match the requested training day.
        if day_type is not None and workout["day_type"] != day_type.upper():
            continue
        # Skip workouts below the requested energy level.
        if min_energy is not None and workout["energy"] < min_energy:
            continue

        matching_workouts.append(workout)

    return matching_workouts

# Create a workout using the same validation function as the CLI.
@app.post("/workouts")
def add_workout(workout_data: WorkoutCreate):

    try:
        workout = create_workout(workout_data.date, workout_data.day_type, workout_data.duration_minutes, workout_data.energy)
    # Report invalid workout values as an HTTP error with the original message.
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))

    # Find the highest existing ID so the new workout receives the next number.
    highest_id = 0
    for existing_workout in workouts:
        if existing_workout["id"] > highest_id:
            highest_id = existing_workout["id"]

    # Assign an ID and start the new workout with no exercises.
    workout["id"] = highest_id + 1
    workout["exercises"] = []
    # Store the workout in memory so the GET endpoints can retrieve it.
    workouts.append(workout)
    
    return workout

# Look up a single workout by its ID.
@app.get("/workouts/{workout_id}")
def read_workout(workout_id: int):
    for workout in workouts:
        if workout["id"] == workout_id:
            return workout
    # Report a missing workout only after checking the entire list.
    raise HTTPException(status_code=404, detail="Workout not found")
