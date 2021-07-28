from django.shortcuts import render, redirect
from .models import Blogs, Comment
from .forms import AddComment
from django.contrib import messages
# Create your views here.
def blogsPage(request):
	"""function to render the blogs page"""

	#variable to collect all blog queries
	blogs = Blogs.objects.all().order_by('pub_date')

	#variable to collect all the comment queries
	comments = Comment.objects.all().reverse()

	#dictionary to pass all the blog and comment queries as a variable
	context = {'blogs':blogs,'comments':comments}

	return render(request, 'blogs.html', context)

def addComment(request):
	"""function to render the page where you can leave comments"""

	#we want to pass the form as an argument
	context = {'form':AddComment}

	#if the POST request was sent by user we must check it and if its correct we save it and add it to DB
	if request.method == "POST":
		form = AddComment(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, "Comment created!" )
			return redirect('blogsPage')

	return render(request, 'comment.html', context)
