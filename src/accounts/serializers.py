from rest_framework import serializers;
from .models import CommonUserProfile;

class CommonUserProfileSerializer(serializers.Serializer):
    class Meta:
        model = CommonUserProfile;
        fields = ['id' , 'email' , 'first_name' , 'last_name' , 'profile_type' , 'password']
