from rest_framework import serializers
from user_1.models import  Doctor_and_Nurse,Staff,Patients,Booking

class data_of_DandN(serializers.ModelSerializer):
    class Meta:
        model=Doctor_and_Nurse
        fields='__all__'

class data_of_Staff(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields='__all__'

class data_of_Patients(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields='__all__'