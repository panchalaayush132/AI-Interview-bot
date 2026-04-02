import os
import json
import google.generativeai as genai

def analyze_resume_with_gemini(resume_text):
    """
    Sends resume text to Gemini and gets a JSON response with score and feedback.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == 'your_gemini_api_key_here':
        return {"score": 0, "feedback": "API Key not configured in .env"}
        
    from .utils import get_gemini_model
    model = get_gemini_model()
    
    prompt = f"""
    You are an expert HR manager and technical recruiter. Review the following resume text and provide a score out of 100 based on its professional quality, clarity, experience, and impact.
    Provide a brief feedback summary (strengths/weaknesses).
    
    Return EXACTLY a valid JSON object with this structure:
    {{
        "score": 85,
        "feedback": "Strong experience but lacks specific metric-based accomplishments."
    }}
    
    Resume Text:
    {resume_text}
    """
    
    try:
        response = model.generate_content(prompt)
        text_response = response.text.strip()
        
        # Clean up markdown code blocks if gemini returns them
        if text_response.startswith("```json"):
            text_response = text_response.strip("```json").strip("```").strip()
        elif text_response.startswith("```"):
            text_response = text_response.strip("```").strip()
            
        data = json.loads(text_response)
        
        # Ensure correct types are returned
        return {
            "score": int(data.get("score", 0)),
            "feedback": str(data.get("feedback", "No feedback provided."))
        }
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return {"score": 0, "feedback": f"Error parsing response: {str(e)}"}
