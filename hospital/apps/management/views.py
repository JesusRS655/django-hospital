from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Department, Director, Patient, Doctor
from .forms import DirectorForm, DepartmentForm, DoctorForm, PatientForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def director_list(request):
    directors = Director.objects.all()
    return render(request, 'directorlist.html', {'directors': directors})

def directorform(request):
    if request.method=='POST':
        director_form = DirectorForm(request.POST)
        if director_form.is_valid():
            director_form.save()
            return redirect('/management/directorlist')
    else:
        director_form = DirectorForm()
    
    return render(request, 'directorform.html', {'form': director_form})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departmentlist.html', {'departments': departments})

def departmentform(request):
    if request.method=='POST':
        department_form = DepartmentForm(request.POST)
        if department_form.is_valid():
            department_form.save()
            return redirect('/management/departmentlist')
    else:
        department_form = DepartmentForm()

    return render(request, 'departmentform.html', {'form': department_form})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctorlist.html', {'doctors': doctors})

def doctorform(request):
    if request.method=='POST':
        doctor_form = DoctorForm(request.POST)
        if doctor_form.is_valid():
            doctor_form.save()
            return redirect('/management/doctorlist')
    else:
        doctor_form = DoctorForm()

    return render(request, 'doctorform.html', {'form': doctor_form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patientlist.html', {'patients': patients})

def patientform(request):
    if request.method=='POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('/management/patientlist')
    else:
        patient_form = PatientForm()
        
    return render(request, 'patientform.html', {'form': patient_form})