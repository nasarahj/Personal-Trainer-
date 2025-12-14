from pydantic import BaseModel, Field
from typing import List, Optional, Union

class Exercise(BaseModel):
    name: str 
    sets: Optional[int] = None
    reps: Optional[int] = None
    duration_seconds: None
    notes: Optional[str] = None

class WorkoutPlan(BaseModel):
    workout_name: str
    duration_minutes: int 
    level: str
    focus: str
    exercises: List[Exercise]   
    safety_notes: Optional[str] = None
    
