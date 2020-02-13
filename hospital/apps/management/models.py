from django.db import models

# Create your models here.

class Director(models.Model):
    dni = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=False, null=False)

    class Meta:
            verbose_name = "Director"
            verbose_name_plural = "Directors"
            ordering = ["last_name"]

    def __str__(self):
        return self.last_name + ", " + self.name

class Department(models.Model):
    director_id = models.OneToOneField(Director, on_delete=models.CASCADE, null=False, primary_key=True) # director del departamento
    code = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["code"]

    def __str__(self):
        return str(self.code) + " - " + self.name

class Doctor(models.Model):
    dni = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=False, null=False)
    hire_date = models.DateField('Hire date', auto_now=False, auto_now_add=True)
    dep = models.ForeignKey(Department, on_delete=models.CASCADE) # departamento al que pertenece

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        ordering = ["last_name"]

    def __str__(self):
        return self.last_name + ", " + self.name

class Patient(models.Model):
    dni = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    picture = models.ImageField(upload_to="img")
    doc = models.ManyToManyField(Doctor) # doctor/es que trata/n al paciente

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        ordering = ["last_name"]

    def __str__(self):
        return self.last_name + ", " + self.name