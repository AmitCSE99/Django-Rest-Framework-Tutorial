from django.urls import path
from . import views
urlpatterns = [
    path("create",views.curd_create),
    path("read-all",views.curd_read_all),
    path("read-one/<int:pk>",views.curd_read_one),
    path('update-one',views.curd_update)
]
