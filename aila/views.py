from django.shortcuts import render

# Create your views here.
def ailaPage(request):
	"""Rendering Daniil's page"""

	return render(request, 'aila.html')