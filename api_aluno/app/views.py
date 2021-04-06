from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from app.models import StudentRegistration
from app.serializers import StudentRegistrationSerializer


class StudentListAndCreate(APIView):
    def get(self, request):
        registration = StudentRegistration.objects.all()
        serializer = StudentRegistrationSerializer(registration, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentChangeAndDelete(APIView):
    def get_object(self, pk):
        try:
            return StudentRegistration.objects.get(pk=pk)
        except StudentRegistration.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentRegistrationSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentRegistrationSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)