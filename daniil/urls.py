from django.urls import path
from . import views

urlpatterns = [
    path('', views.dannilPage, name='dannilPage'),

    #path for exporting a test document
    path('download_pdf_file', views.download_pdf_file, name='download_pdf_file')
]
