from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Registration,Doctor_and_Nurse,Patients,Staff,Booking
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import csrf_exempt
from .serializer import data_of_DandN,data_of_Staff,data_of_Patients
from django.middleware.csrf import get_token
from django.contrib.auth import login,logout,authenticate
from django.db.models import Q

# from .templates import html
# Create your views here.


def get_csrf_token(request):
    csrf_token=get_token(request)
    return JsonResponse({"csrftoken":csrf_token})

# @csrf_exempt
def Register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        name=request.POST.get('name')
        catagory=request.POST.get('catagory')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        password=request.POST.get('password')
        gender=request.POST.get('gender')

        if Registration.objects.filter(Username=username).exists():
            return JsonResponse({'error':'The username is already taken'})
        else:
            if catagory=='Doctor' or catagory=='Nurse':
                Doctor_and_Nurse.objects.create(Username=username,Name=name,Phone=phone,Email=email,Address=address,Catagory=catagory,Gender=gender)
                Registration.objects.create(Username=username,Name=name,Catagory=catagory,Phone=phone,Email=email,Address=address,Gender=gender,
                                            Password=make_password(password))

            elif catagory=='Patients' :
                 Patients.objects.create(Username=username,Name=name,Phone=phone,Email=email,Address=address,Gender=gender)
                 Registration.objects.create(Username=username,Name=name,Catagory=catagory,Phone=phone,Email=email,Address=address,Gender=gender,
                                             Password=make_password(password))

            else:
                 Staff.objects.create(Username=username,Name=name,Phone=phone,Email=email,Address=address,Catagory=catagory,Gender=gender)
                 Registration.objects.create(Username=username,Name=name,Catagory=catagory,Phone=phone,Email=email,Address=address,Gender=gender,
                                             Password=make_password(password))
            
            return JsonResponse({"success":"Your Registration completed"})
    else:
        return JsonResponse({"error":"the method is wrong"})


def login(request):
   
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if request.session.get('user_id'):

            return JsonResponse({
                'message':'User already logged in',
                'status':'success',
                'username': request.session.get('phone')
            })
        
        if Registration.objects.filter(Username=username).exists():
            data=Registration.objects.get(Username=username)

            if data.Username==username and check_password(password,data.Password):
                # request.session['name']=username
                respones= JsonResponse({'success':'login successfully'})
                respones.set_cookie('login_cookie','cookie_value',max_age=3600)

                request.session['username']=data.Username
                request.session['user_id']=data.id

                csrf_token=get_token(request)
                respones.set_cookie('csrftoken',csrf_token)

                return respones
            else:
                 return JsonResponse({'error':'password is wrong'})
        else:
            return JsonResponse({'error':'username not found' })
    else:
        return JsonResponse({'error':'the method is wrong'})
    
@csrf_exempt
def logouts(request):
    
    logout(request)
    response= JsonResponse({'message':'logout successfully'})
    response.delete_cookie('login_cookie')
    response.delete_cookie('csrftoken')
    

    return response
    
@csrf_exempt
def Add_data_of_Doctors_Nurse(request):

    if request.method=="POST":
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        department=request.POST.get('dept')
        image=request.FILES.get('image')
        certificate=request.FILES.get('certificate')
        start=request.POST.get('start_time')
        end=request.POST.get('End_time')
        age=request.POST.get('age')
        dob=request.POST.get('date_of_birth')
        gender=request.POST.get('gender')


        if Doctor_and_Nurse.objects.filter(Username=username).exists():
           data= Doctor_and_Nurse.objects.get(Username=username)
           datas=Registration.objects.get(Username=username)
           datas.Phone=data.Phone=phone
           datas.Email=data.Email=email
           data.Address=datas.Address=address
           data.Department=department
           data.Image=image
           data.Certificate=certificate
           data.Start_Duty_time=start
           data.End_Duty_time=end
           data.Age=age
           data.DOB=dob
           data.Gender=gender
           data.save()
           datas.save()

           return JsonResponse({'success':'data entry successfully'})
        else:
            return JsonResponse({'error':'user not found , try after Registration'})
    
    else:
        return JsonResponse({'error':'method is wrong'})
        
@csrf_exempt
def Add_data_of_staff(request):
    if request.method=="POST":
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        department=request.POST.get('dept')
        image=request.FILES.get('image')
        certificate=request.FILES.get('certificate')
        start=request.POST.get('start_time')
        end=request.POST.get('End_time')
        age=request.POST.get('age')
        dob=request.POST.get('date_of_birth')
        gender=request.POST.get('gender')

        if Staff.objects.filter(Username=username).exists():
           data=Staff.objects.get(Username=username)
           datas=Registration.objects.get(Username=username)
           data.Phone=datas.Phone=phone
           data.Email=datas.Email=email
           data.Address=datas.Address=address
           data.Department=department
           data.Image=image
           data.Certificate=certificate
           data.Start_Duty_time=start
           data.End_Duty_time=end
           data.Age=age
           data.DOB=dob
           data.Gender=gender
           data.save()
           datas.save()

           return JsonResponse({'success':'data entry successfully'})
        else:
            return JsonResponse({'error':'user not found , try after Registration'})
    
    else:
        return JsonResponse({'error':'method is wrong'})
        
@csrf_exempt
def Add_data_of_Patients(request):
    if request.method=="POST":
       username=request.POST.get('username')
       Phone=request.POST.get('phone')
       email=request.POST.get('email')
       address=request.POST.get('address')
       image=request.FILES.get('image')
       doctor=request.POST.get('doctor')
       age=request.POST.get('age')
       dob=request.POST.get('date_of_birth')
       gender=request.POST.get('gender')


       if Patients.objects.filter(Username=username).exists():
           data=Patients.objects.get(Username=username)
           datas=Registration.objects.get(Username=username)
           data.Phone=datas.Phone=Phone
           data.Email=datas.Email=email
           data.Address=datas.Address=address
           data.Image=image
           data.Consultent_Doctor=doctor
           data.Age=age
           data.DOB=dob
           data.Gender=gender
           data.save()
           datas.save()

           return JsonResponse({'success':'patient data entry successfully'})
       else:
           return JsonResponse({'error':'user not found, try after registrations'})
    else:
        return JsonResponse({'error':'method is wrong'})

@csrf_exempt

def booking(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        dob=request.POST.get('date_of_birth')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        email=request.POST.get('email')
        doctor=request.POST.get('Doctor')
        dept=request.POST.get('department')
        date=request.POST.get('Date')
        time=request.POST.get('Time')
        gender=request.POST.get('gender')
        
        if Booking.objects.filter(Phone=phone).exists():
            return JsonResponse({'error':"your are aleady booked"})
        else:
            try:
                 last_token=Booking.objects.all().order_by('Token').last()
                 new_token=last_token.Token+1
            
                 Booking.objects.create(Name=name,Age=age,DOB=dob,Phone=phone,Address=address,Email=email,
                               Appointment_Doctor=doctor,Appointment_dept=dept,Appointment_Date=date,
                               Appointment_Time=time,Gender=gender,Token=new_token)
                 return JsonResponse({'success':'your booking successfully',
                                 'Appointment_Doctor':doctor,
                                 'Appointment_Date':date, 
                                 'Appointment_Time':time ,
                                 'Token number is':new_token})
            except:
                Booking.objects.create(Name=name,Age=age,DOB=dob,Phone=phone,Address=address,Email=email,
                               Appointment_Doctor=doctor,Appointment_dept=dept,Appointment_Date=date,
                               Appointment_Time=time,Gender=gender)
                return JsonResponse({'success':'your booking successfully',
                                 'Appointment_Doctor':doctor,
                                 'Appointment_Date':date, 
                                 'Appointment_Time':time ,
                                 'Token number is':"100"})
    else:
      return JsonResponse({'error':'The method is wrong'})

@csrf_exempt
def delete_booking(request):

    phone=request.POST.get('phone')

    if Booking.objects.filter(Phone=phone).exists():
        Booking.objects.get(Phone=phone).delete()
        return JsonResponse({'success':"The booking has been deleted"})
    else:
        return JsonResponse({'error':'you have   booking'})


@csrf_exempt 
def delete_data_of_person(request):
    if request.method=='POST':
        username=request.POST.get('username')

        if Registration.objects.filter(Username=username).exists():
           data= Registration.objects.get(Username=username)
           datas=data.Catagory

           if datas=='Doctor' or datas=='Nurse':
               Doctor_and_Nurse.objects.get(Username=username).delete()
               Registration.objects.get(Username=username).delete()

               return JsonResponse({'status':'successfully delete all datas of the Doctor or Nurse'})
           
           elif datas=='Patients':
               Patients.objects.get(Username=username).delete()
               Registration.objects.get(Username=username).delete()
               
               return JsonResponse({'status':'successfully delete all datas of the Patient'})
           else:
               Staff.objects.get(Username=username).delete()
               Registration.objects.get(Username=username).delete()

               return JsonResponse({'status':'successfully delete all datas of the Staff'})
        else:
           return JsonResponse({'error':'user not found'})
           

@csrf_exempt
def display_data_of_DandN(request):
    
        
         username=request.POST.get('username')
         
         if Doctor_and_Nurse.objects.filter(Username=username).exists():
             data=Doctor_and_Nurse.objects.get(Username=username)

             serializer=data_of_DandN(data)

             return JsonResponse({'status':'success','data':serializer.data})
           
         else:
             return JsonResponse({'error':'User not found'})

@csrf_exempt
def display_data_of_staff(request):
        
         username=request.POST.get('username')
         
         if Staff.objects.filter(Username=username).exists():
             data=Staff.objects.get(Username=username)

             serializer=data_of_Staff(data)

             return JsonResponse({'status':'success','data':serializer.data})
         else:
             return JsonResponse({'error':'User not found'})


@csrf_exempt
def display_data_of_Patients(request):
        
         username=request.POST.get('username')
         
         if Patients.objects.filter(Username=username).exists():
             data=Patients.objects.get(Username=username)

             serializer=data_of_Patients(data)
             return JsonResponse({'status':'success','data':serializer.data})
         else:
             return JsonResponse({'error':'User not found'})

          


def search_for_doctor(request,name):
    

    if name :

        data = Doctor_and_Nurse.objects.filter(Name__icontains=name) | Doctor_and_Nurse.objects.filter(Phone__icontains=name) | Doctor_and_Nurse.objects.filter(Email__icontains=name)  | Doctor_and_Nurse.objects.filter(Addrass__icontains=name)

        serializer=data_of_DandN(data,many=True)

        return JsonResponse({'status':'success','data':serializer.data})
    else:
        return JsonResponse({'error':"no user found"})



def search_for_staff(request,name):
    
    if name :
        data= Staff.objects.filter(Q(Name__icontains=name) | Q(Phone__icontains=name)| Q(Email__icontains=name)| Q(Address__icontains=name))
        serializer=data_of_Staff(data,many=True)

        return JsonResponse({'status':'success','data':serializer.data})
        # return HttpResponse(data)
    else:
        return JsonResponse({'error':"no user found"})



def search_for_patients(request,name):
    
    
    if name :
        data=Patients.objects.filter(Q(Name__icontains=name) | Q(Phone__icontains=name)| Q(Email__icontains=name)| Q(Address__icontains=name))
        serializer = data_of_Patients(data, many=True)

        return JsonResponse({'status':'success','data':serializer.data})
    else:
        return JsonResponse({'error':"no user found"})
