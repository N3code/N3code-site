from django.shortcuts import render

# Create your views here.
def renatoPage(request):
	"""Rendering Renato's page"""

	return render(request, 'renato.html')