from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination


class StudentListPagination(PageNumberPagination):
    page_size = 4


class StudentListLimitOffset(LimitOffsetPagination):
    default_limit = 4
