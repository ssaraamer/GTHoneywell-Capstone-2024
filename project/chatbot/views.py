from django.shortcuts import render

# Create your views here.
# chatbot/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .llm import get_response

@csrf_exempt  # Exempt this view from CSRF verification; adjust according to your security needs
@require_POST  # Ensure that this view can only handle POST requests
def chatbot_view(request):
    try:
        data = json.loads(request.body)
        user_input = data.get('message')
        bot_response = get_response(user_input)
        return JsonResponse({'response': bot_response})
    except Exception as e:
        return JsonResponse({'error': str(e)})