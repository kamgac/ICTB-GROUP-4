
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('input_video/', views.input_video, name='input_video'),
]
