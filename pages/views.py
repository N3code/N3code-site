from django.shortcuts import render
from blogs.models import Blogs

#All good time to get serious!

# Create your views here. Any time you create a new html page, it needs a view in order to load it. You will also need to create a url for it.

def aboutPage(request):
	"""function to render
	about page and display
	the latest blog"""

	#collect 3 latest blogs and display them on the page
	last_blog_0 = Blogs.objects.all().reverse()[0]
	last_blog_1 = Blogs.objects.all().reverse()[1]
	last_blog_2 = Blogs.objects.all().reverse()[2]

	#context dictionary to render the latest blog on the page
	context = {
	'last_blog_0':last_blog_0,
	'last_blog_1':last_blog_1,
	'last_blog_2':last_blog_2
	}

	return render(request, 'about.html', context)

def comingSoonPage(request):
	"""fucntion to return the
	coming soon page
	which will be applied to
	every page which is not finished"""

	return render(request, 'coming.html')

def personalPageEg(request):
	"""function to
	load the personal page"""

	return render(request, 'personal_page_eg.html')
