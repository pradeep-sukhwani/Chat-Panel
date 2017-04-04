from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from chat_app import settings

from .models import Chat

def home_page(request):
    return render(request, 'alpha/home_page.html')

def login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "alpha/login.html", {'next': next})

def logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def chat_panel(request):
    c = Chat.objects.all()
    return render(request, "alpha/chat_panel.html", {'home': 'active', 'chat': c})

def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

def messages(request):
    c = Chat.objects.all()
    return render(request, 'alpha/messages.html', {'chat': c})
