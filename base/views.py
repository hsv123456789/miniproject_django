from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    return render(request, 'login.html')


def form_submit(request):
    if request.method == 'POST':
        return redirect('home')
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def mlmodel(request):
    return render(request,'mlmodel.html')