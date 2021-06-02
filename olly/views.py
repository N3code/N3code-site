from django.shortcuts import render

# Create your views here.
def ollyPage(request):
	return render(request, 'olly.html')