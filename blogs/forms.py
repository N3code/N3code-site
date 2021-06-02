from django.forms import ModelForm
from .models import Comment

class AddComment(ModelForm):
	"""this is the class to add the comment"""
	class Meta:

		#this references the model from which it should take the fields
		model = Comment

		#this tells django that I want to use all the fields referenced in the model
		fields = '__all__'