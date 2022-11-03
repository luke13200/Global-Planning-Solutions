from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index_view(request):
    """
    URL: /
    this view is for the static landing page.
    """
    return render(request, 'user/index.html', None);

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('<h1>Login failed</h1>')

    else:
        return render(request, 'user/login.html', None)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
