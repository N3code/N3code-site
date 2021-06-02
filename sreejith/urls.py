from django.urls import path
from . import views

urlpatterns = [
    path('', views.sreejithPage, name='sreejithPage')
]