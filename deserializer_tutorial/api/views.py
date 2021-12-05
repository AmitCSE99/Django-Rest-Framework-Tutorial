from django.shortcuts import render
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':"Data Created Sucessfully"})
        return JsonResponse({'msg':"failed"})

