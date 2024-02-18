from rest_framework import serializers
from .models import Teacher
from django.contrib.auth import get_user_model


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Teacher


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')
