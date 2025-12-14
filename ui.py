import gradio as gr
from app.coach import coach_response

def build_ui():
    def chat_fn(message, history):
        user_id = "default"
        response = coach_response(message, user_id=user_id)
        return response
    
    app = gr.ChatInterface(
        fn =chat_fn,
        title="AI Fitness Coach",
        description=(
            "Ask me about workouts, routines, or healthy habits."
    ),
    examples=[
        "Give me a 15-minute beginner workout",
        "I have knee pain—what exercises should I avoid?",
        "Create a weekly plan for a beginner",
        "How can I stay motivated to exercise regularly?"
    ],
 )
    return app