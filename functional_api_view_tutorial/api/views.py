from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# @api_view(['GET'])
# def test_view(request):
#     return Response({'success':True,'data':'This is a test'})

@api_view(['POST'])
def test_view(request):
    if request.method=='POST':
        print(request.data.get("name"))
        return Response({'success':True,'data':"This is from post request"})