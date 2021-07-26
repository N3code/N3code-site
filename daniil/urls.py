from django.urls import path
from . import views

urlpatterns = [
    path('', views.dannilPage, name='dannilPage'),

    #path for exporting a test document
    path('export-pdf', views.exportCertificate, name='export-pdf')
]
