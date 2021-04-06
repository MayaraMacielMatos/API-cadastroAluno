from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from app.models import StudentRegistration
from app.serializers import StudentRegistrationSerializer


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        registration = StudentRegistration.objects.all()
        serializer = StudentRegistrationSerializer(registration, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_delete(request, pk):
    try:
        student = StudentRegistration.objects.get(pk=pk)
    except StudentRegistration.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentRegistrationSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentRegistrationSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)