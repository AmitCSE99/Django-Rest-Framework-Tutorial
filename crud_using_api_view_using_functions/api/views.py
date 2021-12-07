from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def get_student_data(request):
    id = request.data.get('id')
    if id is not None:
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu)
        return Response({'success': True, 'data': serializer.data})
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return Response({'success': True, 'data': serializer.data})


@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': request.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_student(request):
    id = request.data.get('id')
    stu = Student.objects.get(pk=id)
    serializer = StudentSerializer(stu, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True, 'data': request.data})
    return Response({'success': False, 'message': serializer.errors})
