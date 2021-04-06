from rest_framework import generics

from app.models import StudentRegistration
from app.serializers import StudentRegistrationSerializer


class StudentListAndCreate(generics.ListCreateAPIView):
    queryset = StudentRegistration.objects.all()
    serializer_class = StudentRegistrationSerializer


class StudentChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentRegistration.objects.all()
    serializer_class = StudentRegistrationSerializer