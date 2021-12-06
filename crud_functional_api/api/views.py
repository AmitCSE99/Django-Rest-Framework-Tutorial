from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from .serializers import StudentSerializer
from .models import Student
from rest_framework.parsers import JSONParser
import io
# Create your views here.
def curd_create(request):
    json_data=request.body
    stream=io.BytesIO(json_data)
    python_data=JSONParser().parse(stream=stream)
    serializer=StudentSerializer(data=python_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success':True})
    return JsonResponse({'success':False})

def curd_read_all(request):
    student_list=Student.objects.all()
    serializer=StudentSerializer(student_list,many=True)
    return JsonResponse(serializer.data,safe=False)


def curd_read_one(request,pk):
    student=Student.objects.get(id=pk)
    serializer=StudentSerializer(student)
    return JsonResponse(serializer.data,safe=False)

def curd_update(request):
    json_data=request.body
    stream=io.BytesIO(json_data)
    python_data=JSONParser().parse(stream=stream)
    id=python_data.get('id')
    stu=Student.objects.get(id=id)
    serializer=StudentSerializer(stu,python_data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success':True},safe=False)
    return JsonResponse({'success':False})
