from django.urls import path
from . import views

urlpatterns = [
    path('', views.ollyPage, name='ollyPage')
]