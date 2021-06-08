from django.forms import ModelForm
from .models import Comment

class AddComment(ModelForm):
	"""this is the class to add the comment"""
	class Meta:

		#this references the model from which it should take the fields
		model = Comment

		#Naming each field like it was specified in models.py so that I can reference them in html forms
		fields = ['blog','name','comment']