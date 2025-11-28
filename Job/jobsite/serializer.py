from rest_framework import serializers
from jobsite.models import Company,Job

from jobsite.models import CustomUser


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model= CustomUser
        fields=['first_name','last_name','username','password','email','role']

    def create(self, validated_data):
        user=CustomUser.objects.create_user(**validated_data)
        return user