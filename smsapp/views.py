from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages

# Create your views here.

def login_view(request):
    # Default login for now
    usr = 'teacher'
    pwd = '12345'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == usr and password == pwd:
            return redirect('home')
        else: 
            messages.success(request, 'Please enter valid username and password')
    else:
        msg = messages.error(request, 'Huh......')
    return render(request, 'login.html', {'message': msg})

def home(request):
    data = Student.objects.all()
    return render(request, 'home.html', {'data': data})

def create(request):
    if request.method == 'POST':
        data = StudentForm(request.POST)
        if data.is_valid():
            data.save()
            msg = messages.success(request, 'Record created successfully')
            fm = StudentForm()
            return render(request, 'create.html', {'fm': fm, 'msg': msg})
        else:
            msg = messages.error(request, 'Check error')
            return render(request, 'create.html', {'fm': data, 'msg': msg})
    else:
        fm = StudentForm()
        return render(request, 'create.html', {'fm':fm})