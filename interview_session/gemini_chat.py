import os
import google.generativeai as genai

def serialize_history(history):
    serialized = []
    for msg in history:
        # Handling the text extraction safely
        parts = [part.text for part in msg.parts]
        serialized.append({"role": msg.role, "parts": parts})
    return serialized

def get_interviewer_response(candidate_context, chat_history, user_message):
    """
    Sends the user message to Gemini using the existing chat history.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == 'your_gemini_api_key_here':
        return "API Key not configured.", chat_history

    from candidates.utils import get_gemini_model
    model = get_gemini_model()

    if not chat_history:
        # Initiate the conversation with context
        system_instruction = f"""You are a professional HR Interviewer for a tech company interviewing a candidate based on this resume:
{candidate_context}

Follow this strict interview flow:
1. Start with a basic HR introduction question.
2. Move to basic fundamentals based on their specific skills (e.g., if Python, "What is a list?").
3. Ask medium technical questions.

RULES:
- Ask exactly ONE question at a time.
- Keep your responses VERY SHORT and conversational (1-2 sentences max). Do NOT write paragraphs.
- Act like a real human.
- The candidate just said: {user_message}"""
        
        chat = model.start_chat(history=[])
        try:
            response = chat.send_message(system_instruction)
            return response.text, serialize_history(chat.history)
        except Exception as e:
            return f"Error connecting to AI: {str(e)}", []
    else:
        # Reconstruct history
        formatted_history = []
        for msg in chat_history:
            formatted_history.append({
                "role": msg["role"],
                "parts": msg["parts"]
            })
            
        chat = model.start_chat(history=formatted_history)
        try:
            response = chat.send_message(user_message)
            return response.text, serialize_history(chat.history)
        except Exception as e:
            return f"Error during chat: {str(e)}", chat_history
