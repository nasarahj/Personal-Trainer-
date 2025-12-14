import os
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import User
from langchain_openai import ChatOpenAI
from app import memory
from app.prompts import SYSTEM_PROMPT
from app.memory import load_memory, save_memory
from app.schemas import WorkoutPlan
from langchain_core.output_parsers import PydanticOutputParser
from app.tools import exercise_safety_lookup



# Load environment variables from .env file
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

# Initialize the language model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
)

def coach_response(user_message: str, user_id: str = "default") -> str:
    memory = load_memory(user_id)
    injury = None

    if "injuries" in memory and memory["injuries"]:
        injury = memory["injuries"][0]

    tool_context = ""

    if injury and "safe" in user_message.lower():
    # naive extraction of exercise name
       exercise = user_message.replace("safe", "").strip()

       tool_result = exercise_safety_lookup(exercise, injury)

    tool_context = f"""
Tool result (exercise safety check):
{tool_result}
"""
   
        
    memory_context = f"User profile: {memory}" if memory else ""


    prompt = f"""
{SYSTEM_PROMPT}

{memory_context}

{tool_context}

If a tool result is provided, use it to guide your answer.

User message:
{user_message}
"""

    #Call LLM
    result = llm.invoke(prompt).content

     # Structured output parsing (already implemented)
    try:
        plan = parser.parse(result)
        return render_workout_plan(plan)
    except Exception:
        return result