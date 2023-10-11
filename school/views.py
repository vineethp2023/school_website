from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def profile(request):
    return render(request, 'profile.html', {'profile': 'enabled'})


def order(request):
    return render(request, 'order.html', {'profile': 'enabled'})


