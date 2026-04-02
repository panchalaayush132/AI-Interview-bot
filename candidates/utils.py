import fitz # PyMuPDF
import os
import google.generativeai as genai

_best_model = None

def get_gemini_model():
    global _best_model
    if _best_model:
        return genai.GenerativeModel(_best_model)
    
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        for preferred in ['models/gemini-1.5-flash', 'models/gemini-1.5-flash-latest', 'models/gemini-1.0-pro', 'models/gemini-pro']:
            if preferred in available_models:
                _best_model = preferred
                break
                
        if not _best_model:
            _best_model = available_models[0] if available_models else 'gemini-pro'
    except Exception as e:
        print("Error listing models:", e)
        _best_model = 'gemini-pro'
        
    print(f">>> Auto-selected Gemini Model: {_best_model}")
    return genai.GenerativeModel(_best_model)

def extract_text_from_pdf(file_path):
    """
    Extracts underlying text blocks from a PDF file using PyMuPDF.
    """
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
        return ""
