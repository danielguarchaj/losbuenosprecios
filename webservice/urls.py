  
from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'webservice'

urlpatterns = [
    path('productos/', views.ProductoList.as_view(), name='productos')
]