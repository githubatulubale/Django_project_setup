from django.urls import path
from . import views   # name of the file

urlpatterns = [
    path('', views.index),   # (name you can put you want  / ) file name . function name, 
    
]
