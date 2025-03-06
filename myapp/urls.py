from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("todo", views.home, name='todos'),
]