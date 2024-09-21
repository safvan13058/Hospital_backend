from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

#   Registrations
 
class Registration(models.Model):
    Username=models.CharField(max_length=50)
    Name=models.CharField(max_length=100)
    Catagory=models.CharField(max_length=50)
    Gender=models.CharField(max_length=20,null=True,blank=True)
    Phone=models.CharField(max_length=12)
    Email=models.EmailField()
    Address=models.TextField()
    Password=models.CharField(max_length=100)
    Time=models.DateTimeField(auto_now_add=True)

#     #  login

# class Login(models.Model):
#     User_name=models.CharField(max_length=100)
#     Pass_word=models.CharField(max_length=100)
#     attempt=models.CharField(max_length=300)
#     Time=models.DateTimeField(auto_now_add=True)
   
    #  Doctor_and_Nurse details
    
class Doctor_and_Nurse(models.Model):
    Username=models.CharField(max_length=50)
    Name=models.CharField(max_length=100)
    
    DOB=models.DateField(null=True,blank=True)
    Gender=models.CharField(max_length=20,null=True,blank=True)
    Phone=models.CharField(max_length=12)
    Age=models.IntegerField(null=True,blank=True)
    Email=models.EmailField()
    Address=models.TextField()
    Catagory=models.CharField(max_length=50)
    Department=models.CharField(max_length=50,null=True,blank=True)
    Image=models.ImageField(upload_to='profile/',null=True,blank=True)
    Certificate=models.FileField(upload_to='Certificate',null=True,blank=True)
    Start_Duty_time=models.TimeField(null=True,blank=True)
    End_Duty_time=models.TimeField(null=True,blank=True)

    # Staff details

class Staff(models.Model):
    Username=models.CharField(max_length=50)
    Name=models.CharField(max_length=100)
    Age=models.IntegerField(null=True,blank=True)
    DOB=models.DateField(null=True,blank=True)
    Gender=models.CharField(max_length=20,null=True,blank=True)
    Phone=models.CharField(max_length=12)
    Email=models.EmailField()
    Address=models.TextField()
    Catagory=models.CharField(max_length=50,null=True,blank=True)
    Department=models.CharField(max_length=50,null=True)
    Image=models.ImageField(upload_to='profile/',null=True)
    Certificate=models.FileField(upload_to='Certificate',null=True,blank=True)
    Start_Duty_time=models.TimeField(null=True)
    End_Duty_time=models.TimeField(null=True)


    #  Patients
    
class Patients(models.Model):
    Username=models.CharField(max_length=50)
    Name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=12)
    Age=models.IntegerField(null=True,blank=True)
    DOB=models.DateField(null=True,blank=True)
    Gender=models.CharField(max_length=20,null=True,blank=True)
    Email=models.EmailField()
    Address=models.TextField()
    Image=models.ImageField(upload_to='patients_photos/',null=True)
    Consultent_Doctor=models.CharField(max_length=100,null=True)


class Booking(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField(null=True,blank=True)
    DOB=models.DateField(null=True,blank=True)
    Gender=models.CharField(max_length=20,null=True,blank=True)
    Phone=models.CharField(max_length=12)
    Address=models.TextField()
    Email=models.EmailField(null=True,blank=True)
    Appointment_Doctor=models.CharField(max_length=100)
    Appointment_dept=models.CharField(max_length=50)
    Appointment_Date=models.DateField()
    Appointment_Time=models.TimeField()
    Token=models.IntegerField(default=100,null=True,blank=True)