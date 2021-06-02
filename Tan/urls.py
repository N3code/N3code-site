from django.urls import path

from . import views 
#test
urlpatterns = [
    #path for tan
    path('', views.TanPage, name = "TanPage" ),


]
