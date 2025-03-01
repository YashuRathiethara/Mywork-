from django.shortcuts import render, redirect 
from django.http import HttpResponse
import datetime
import requests

def hello(request):
    today = datetime.datetime.now().date()
    daysofWeek = ["Mon", "Tue", "Wed", "Thu","Fri", "Sat", "Sun"]
    return redirect("https://www.djangoproject.com")

from formapp.forms import LoginForm

def login(request):
    username = "You're Logged In"
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()
        
    return render(request, 'loggedin.html', {"username": username})


def fetch_users(request):
    api_url = "http://127.0.0.1:5000/users"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        users = data.get('data', [])
    except Exception as e:
        return HttpResponse(f"Error fetching data: {e}", status=500)

    return render(request, 'users.html', {'users': users})



