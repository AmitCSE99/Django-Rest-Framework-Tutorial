from django.urls import path
from . import views
urlpatterns = [
    path("studentapi", views.StudentList.as_view()),
    path("studentcreate", views.StudentCreate.as_view()),
    # path("studentapi/<int:pk>", views.StudentRetreive.as_view())
    path("studentapi/<int:pk>", views.StudentUpdate.as_view())
]
