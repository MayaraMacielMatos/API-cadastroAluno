from app.models import StudentRegistration

from rest_framework import serializers


class StudentRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegistration
        fields = '__all__'
