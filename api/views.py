# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Students 
from .serializers import StudentsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def studentsView(request):
    if request.method == 'GET':
         # Get all the data form the studenht table
        students = Students.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    