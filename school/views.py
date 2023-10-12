from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword:
            error = 'password and confirm password must be matched'
            return render(request,'register.html',{'error':error})
        elif username == '' or password == '':
            error = 'username or password should not be empty'
            return render(request, 'register.html', {'error': error})
        else:
            user = User.objects.create(username=username,email=username,password=cpassword)
            msg = 'Account created successfully'
            return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')


def register(request):
    return render(request, 'register.html')


def profile(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        if username == '' or password == '':
            error = 'User name or password must not be empty'
            return render(request,'login.html',{'error':error})
        else:
            user = User.objects.filter(username=username,password=password)
            if user is not None:
                return render(request, 'profile.html', {'profile': 'enabled'})
            else:
                error = 'Invalid username or password'
                return render(request, 'login.html', {'error': error})


def order(request):
    return render(request, 'order.html', {'profile': 'enabled'})


