from django.urls import path
from .models import User
from . import views
urlpatterns = [
    path("register", views.RegisterView.as_view()),
    path("login", views.LoginView.as_view()),
    path("reset", views.ResetAll.as_view()),
    path("getlist", views.GetUsersList.as_view())
]
