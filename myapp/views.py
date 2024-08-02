from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Employee
from .forms import EmployeeForm

def login_page(request):
    return render(request, 'employees/login.html')

def logout_view(request):
    logout(request)
    return redirect('myapp:login') 

def edit_employee(request):
    return render(request, 'employees/edit.html')
    

def validate_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        if not username or not password:
            return JsonResponse({'success': False, 'error_message': 'Please fill in all fields.'})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error_message': 'Invalid username or password.'})

    return JsonResponse({'success': False, 'error_message': 'Invalid request method.'})

def index(request):
    employees = Employee.objects.all()  
    return render(request, 'employees/index.html', {'employees': employees})

def get_employees(request):
    employees = Employee.objects.all().values('id', 'name', 'email', 'password')
    return JsonResponse(list(employees), safe=False)


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = EmployeeForm()
    
    return render(request, 'employees/add.html', {'form': form})

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employees/edit.html', {'employee': employee})

    
@require_POST
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    
    # Update employee fields
    employee.name = request.POST.get('name')
    employee.email = request.POST.get('email')
    employee.password = request.POST.get('password')
    
    # Save updated employee
    employee.save()
    
    return JsonResponse({'status': 'success'})

@csrf_exempt
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return JsonResponse({'message': 'Employee deleted successfully.'})
    else:
        return JsonResponse({'error': 'POST method required.'}, status=405)
    

def get_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    data = {
        'id': employee.id,
        'name': employee.name,
        'email': employee.email,
        'password': employee.password
    }
    return JsonResponse(data)

