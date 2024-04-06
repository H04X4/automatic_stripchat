from django.shortcuts import render

from .browser_automation import main

def index(request):
    if 'username' in request.POST:
        username = request.POST['username']
        main(username)
    else:
        print("Username отсутствует")
    

    return render(request, '../templates/index.html')



