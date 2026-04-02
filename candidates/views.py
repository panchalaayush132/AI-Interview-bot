from django.shortcuts import render, redirect
from .models import Candidate
from .utils import extract_text_from_pdf
from .gemini_service import analyze_resume_with_gemini

def upload_resume(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume_file = request.FILES.get('resume_file')
        
        if name and email and resume_file:
            # Create Candidate
            candidate = Candidate.objects.create(
                name=name, email=email, resume_file=resume_file
            )
            
            # Extract Text
            try:
                text = extract_text_from_pdf(candidate.resume_file.path)
            except Exception as e:
                text = ""
                print(f"Extraction failed: {e}")
                
            candidate.extracted_text = text
            
            # Score via Gemini
            if text:
                result = analyze_resume_with_gemini(text)
                candidate.gemini_score = result.get('score', 0)
                candidate.feedback_summary = result.get('feedback', '')
            
            candidate.save()
            return redirect('candidates:upload_success')
            
    return render(request, 'candidates/upload_resume.html')

def upload_success(request):
    return render(request, 'candidates/upload_success.html')

def hr_dashboard(request):
    candidates = Candidate.objects.all().order_by('-gemini_score')
    return render(request, 'candidates/hr_dashboard.html', {'candidates': candidates})
