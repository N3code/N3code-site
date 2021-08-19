from django.urls import path
from . import views

urlpatterns = [

    path('', views.ailaPage, name='ailaPage'),

]