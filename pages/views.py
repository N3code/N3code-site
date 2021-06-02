from django.shortcuts import render

#All good time to get serious!

# Create your views here. Any time you create a new html page, it needs a view in order to load it. You will also need to create a url for it.

def aboutPage(request):
	"""function to render about page"""

	return render(request, 'about.html')