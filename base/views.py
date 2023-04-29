from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def form_submit(request):
    return redirect('home')


from django.conf import settings
import os


def upload_files(request):
    if request.method == 'POST':
        # Handle the file upload logic here
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')
        file3 = request.FILES.get('file3')

        if file1:
            # Save file1
            save_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
            file1_path = os.path.join(save_path, file1.name)

            with open(file1_path, 'wb') as destination:
                for chunk in file1.chunks():
                    destination.write(chunk)

        if file2:
            # Save file2
            save_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
            file2_path = os.path.join(save_path, file2.name)

            with open(file2_path, 'wb') as destination:
                for chunk in file2.chunks():
                    destination.write(chunk)

        if file3:
            # Save file3
            save_path = os.path.join(settings.MEDIA_ROOT, 'uploads')
            file3_path = os.path.join(save_path, file3.name)

            with open(file3_path, 'wb') as destination:
                for chunk in file3.chunks():
                    destination.write(chunk)

        # Optionally, you can perform additional operations on the files
        # such as reading the contents, processing the data, etc.

        # Redirect or render a success message
        return render(request, 'home.html')

    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def mlmodel(request):
    return render(request, 'mlmodel.html')
