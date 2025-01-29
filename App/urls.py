from django.urls import path
from .views import *

urlpatterns = [
    path('', user_list, name="home"),
    path('producto/', producto, name="producto"),
]
