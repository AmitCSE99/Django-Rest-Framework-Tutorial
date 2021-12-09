from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from .paginations import StudentListPagination, StudentListLimitOffset
from rest_framework.pagination import LimitOffsetPagination


class GetStudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentListPagination


class GetStudentListFromView(APIView, StudentListLimitOffset):
    def get(self, request):
        student_list = Student.objects.all()
        results = self.paginate_queryset(student_list, request, view=self)
        serializer = StudentSerializer(results, many=True)
        return self.get_paginated_response({'data': serializer.data})
