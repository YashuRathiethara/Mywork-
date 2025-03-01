from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == 'admin' and password == 'abc':
            messages.success(request, 'Login successful')
            return redirect('dashboard.html')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')
