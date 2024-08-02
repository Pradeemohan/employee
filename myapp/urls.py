# employees/urls.py

from django.urls import path
from . import views

app_name = 'myapp' 

urlpatterns = [
    path('', views.login_page, name='login'),
    path('validate-login/', views.validate_login, name='validate_login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('get-employees/', views.get_employees, name='get_employees'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit-employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('update-employee/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('delete-employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('get-employee/<int:employee_id>/', views.get_employee, name='get_employee'),
   
]
