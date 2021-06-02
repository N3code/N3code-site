from django.shortcuts import render

# Create your views here.
def dannilPage(request):
	"""Rendering Daniil's page"""
	
	return render(request, 'daniil.html')