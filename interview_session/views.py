import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from candidates.models import Candidate
from .gemini_chat import get_interviewer_response

def room(request):
    # For a real system, you'd match by user sessions or IDs.
    # Here we just grab the latest candidate scored.
    candidate = Candidate.objects.order_by('-created_at').first()
    context = {}
    if candidate:
        context['candidate_name'] = candidate.name
        context['candidate_text'] = candidate.extracted_text
    else:
        context['candidate_name'] = 'Guest'
        context['candidate_text'] = 'No resume provided.'
        
    return render(request, 'interview_session/room.html', context)

@csrf_exempt
def api_chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            chat_history = data.get("history", [])
            candidate_text = data.get("candidate_text", "")
            
            ai_text, new_history = get_interviewer_response(candidate_text, chat_history, user_message)
            
            return JsonResponse({
                "response": ai_text,
                "history": new_history
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)
