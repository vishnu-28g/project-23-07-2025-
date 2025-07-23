from django.urls import path
from .views import *

urlpatterns = [
    path('',home , name='home'),# API - POSTMAN
    path('index/', index, name='index'),
    path('demo/', demo, name='demo'),
] 