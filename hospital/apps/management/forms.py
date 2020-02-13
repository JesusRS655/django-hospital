from django import forms
from .models import Director, Department, Doctor, Patient

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        labels = {
            'dni': ('DNI:'),
            'name': ('Director\'s name: '),
            'last_name': ('Director\'s last name:')
        }
        widgets = {
            'dni' : forms.TextInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '9 characters max'
            }),
            'name' : forms.TextInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '20 characters max'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '40 characters max'
            })
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['director_id', 'code', 'name']
        labels = {
            'director_id': 'Director\'s name:',
            'code': 'Department code:',
            'name': 'Department name:'
        }
        widgets = {
            'director_id': forms.Select(attrs={
                'class': 'form-control m-2',
            }),
            'code': forms.NumberInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '3 numbers max'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '50 characters max'
            })
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['dni', 'name', 'last_name', 'dep']
        labels = {
            'dni': ('DNI:'),
            'name': ('Doctor\'s name:'),
            'last_name': ('Doctor\'s last name:'),
            'dep': ('Department code:')
        }
        widgets = {
            'dni' : forms.TextInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '9 characters max'
            }),
            'name' : forms.TextInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '20 characters max'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '40 characters max'
            }),
            'dep': forms.Select(attrs={
                'class': 'form-control m-2',
            })
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['dni', 'name', 'last_name', 'age', 'picture', 'doc']
        labels = {
            'dni': ('DNI:'),
            'name': ('Patient\'s name:'),
            'last_name': ('Patient\'s last name:'),
            'age': ('Patient\'s age:'),
            'picture': ('Picture'),
            'doc': ('Treating doctor (use Control Key to select more than one):')
        }
        widgets = {
            'dni' : forms.TextInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '9 characters max'
            }),
            'name' : forms.TextInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '20 characters max'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '40 characters max'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control m-2',
                'placeholder': '3 numbers max'
            }),
            'doc': forms.SelectMultiple(attrs={
                'class': 'form-control m-2'
            })
        }