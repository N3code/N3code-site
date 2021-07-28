from django.urls import path
from . import views

urlpatterns = [
	#all paths for pages app should be written here.

	path('', views.aboutPage, name="aboutPage"),

	#path for coming soon page
	path('coming-soon', views.comingSoonPage, name="comingSoonPage"),

	#path for the personal page
	path('personal-page-eg', views.personalPageEg, name="personal-page-eg")

]
