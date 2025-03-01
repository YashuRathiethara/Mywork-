# Create your views here.
from django.shortcuts import render, redirect
import requests
from employee.forms import EmployeeForm 
from employee.models import Employee
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show')
            except:
                pass
    else:
        form = EmployeeForm()
        return render(request, 'index.html', {'form':form})
    
    
def show(request):
    employee = Employee.objects.all()
    return render(request, 'show.html', {'employee': employee})

def edit(request, id):
    employee = Employee.objects.get(id = id)
    print(employee)
    return render(request, 'edit.html', {'employee': employee})

def update(request, id):
    employee = Employee.objects.get(Employee, id=id) 

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)  # Bind the form with the POST data and the current instance
        if form.is_valid():
            form.save()  # Save the form if valid
            return redirect("show")  # Redirect to the list page after saving
    else:
        form = EmployeeForm(instance=employee)  
    return render(request, 'edit.html', {'form': form, 'employee': employee})

def destroy(request, id):
     employee = Employee.objects.get(id = id)
     employee.delete()
     return redirect("show")

    
def consume_flask_endpoint(request):
    if request.method == 'GET' and 'trigger' in request.GET:
        try:
            flask_url = 'http://127.0.0.1:5000'  # Flask server URL
            response = requests.get(flask_url)

            if response.status_code == 200:
                try:
                    data = response.json()
                    context = {'message': data.get('message', 'No message available')}
                    return render(request, 'consumetemplate.html', context)
                except ValueError:
                    return render(request, 'consumetemplate.html', {'message': 'Invalid JSON response from Flask'})
            else:
                return render(request, 'consumetemplate.html', {'message': f'Flask server returned status: {response.status_code}'})
        except requests.exceptions.RequestException as e:
            return render(request, 'consumetemplate.html', {'message': f'RequestException: {e}'})
        except Exception as e:
            return render(request, 'consumetemplate.html', {'message': f'An error occurred: {e}'})
    
    # Render without any message by default
    return render(request, 'consumetemplate.html')



