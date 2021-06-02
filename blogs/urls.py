from django.urls import path,include
from . import views
urlpatterns = [
    #path for the page with all the blogs and comments
   path('', views.blogsPage, name="blogsPage"),

   #path for the page to create the commnets
   path('addComment', views.addComment, name="addComment")
]