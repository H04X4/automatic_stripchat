from django.shortcuts import render
from django.http import JsonResponse
from .browser_automation import main
import json

def index(request):
    return render(request, 'index.html')

def run_main(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST['username']
            output_json = main(username)

            output_text = json.dumps(output_json, ensure_ascii=False).encode('utf-8')

            return JsonResponse({'output': output_text.decode('utf-8')}, charset='utf-8')
    return JsonResponse({'error': 'Ошибка запроса'}, charset='utf-8')
