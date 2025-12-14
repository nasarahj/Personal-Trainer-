from typing import Dict

def exercise_safety_lookup(exercise: str, injury: str) -> Dict[str, str]:
    """
    Simple safety lookup tool.
    In real systems this could query a database or API.
    """
    exercise = exercise.lower()
    injury = injury.lower()

    unsafe = {
        "knee pain": ["jump", "run", "deep squat", "plyometric"],
        "back pain": ["deadlift", "toe touch", "sit-up"],
    }

    for keyword in unsafe.get(injury, []):
        if keyword in exercise:
            return {
                "safe": "no",
                "reason": f"{exercise.title()} may aggravate {injury}."
            }

    return {
        "safe": "yes",
        "reason": f"No common issues found for {exercise} with {injury}."
    }
