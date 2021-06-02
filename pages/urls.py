from django.urls import path
from . import views

urlpatterns = [
	#all paths for pages app should be written here.

	path('', views.aboutPage, name="aboutPage")
]
