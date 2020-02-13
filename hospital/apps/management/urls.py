from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('index/', index, name='index'),
    path('directorlist/', director_list, name = 'directorlist'),
    path('directorform/', directorform, name = 'directorform'),
    path('departmentlist/', department_list, name = 'departmentlist'),
    path('departmentform/', departmentform, name = 'departmentform'),
    path('doctorlist/', doctor_list, name = 'doctorlist'),
    path('doctorform/', doctorform, name = 'doctorform'),
    path('patientlist/', patient_list, name = 'patientlist'),
    path('patientform/', patientform, name = 'patientform')
]