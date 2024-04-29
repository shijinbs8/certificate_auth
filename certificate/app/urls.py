from django.urls import path
from .views import *


urlpatterns = [
    path('', search_employee, name='search_employee'),
    # path('create/', create_employee, name='create_employee'),
    # path('employees/', view_employees, name='view_employees'),
    path('add/', add_employee_and_skills, name='add-employee'),
    path('employee/<int:employee_id>/', view_employee, name='view_employee_url'),
    path('edit/<int:employee_id>/', edit_employee, name='edit_employee_url'),
    path('api', searchemp_api, name='searchemp_api'),

]
