from django.urls import path
from . import views

urlpatterns = [
    path('', views.dannilPage, name='dannilPage')
]