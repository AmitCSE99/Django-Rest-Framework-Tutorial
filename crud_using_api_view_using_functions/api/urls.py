from django.urls import path
from . import views
urlpatterns = [
    path('get-student-data', views.get_student_data),
    path('create-student-data', views.create_student),
    path('update-student-data', views.update_student)
]
