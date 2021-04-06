from rest_framework import viewsets

from app.models import StudentRegistration
from app.serializers import StudentRegistrationSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentRegistration.objects.all()
    serializer_class = StudentRegistrationSerializer
