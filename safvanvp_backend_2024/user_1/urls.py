from django.urls import path
from .import views

urlpatterns=[
     path('csrftoken',views.get_csrf_token,name='csrftoken'),
     path('Register',views.Register,name='Register'),
     path('login',views.login,name='login'),
     path('logout',views.logouts,name='logout'),
     path('add_data_of_DandN',views.Add_data_of_Doctors_Nurse,name='add data of doctors and nurse'),
     path('add_data_of_staff',views.Add_data_of_staff,name='add_data_of_staff'),
     path('add_data_of_patients',views.Add_data_of_Patients,name='add_data_of_patients'),
     path('display_data_of_DandN',views.display_data_of_DandN,name='display_data_of_DandN'),
     path('display_data_of_staff',views.display_data_of_staff,name='display_data_of_staff'),
     path('display_data_of_Patients',views.display_data_of_Patients,name='display_data_of_Patients'),
     path('delete_data_of_person',views.delete_data_of_person,name='delete_data_of_person'),
     path('booking',views.booking,name='booking'),
     path('delete_booking',views.delete_booking,name='delete_booking'),
     path('searchd/<str:name>',views.search_for_doctor,name='search'),
     path('searchs/<str:name>',views.search_for_staff,name='search'),
     path('searchp/<str:name>',views.search_for_patients,name='search'),
]