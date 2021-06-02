from django.db import models

# Create your models here.
class Blogs(models.Model):
	"""this class will contain all the blogs that we as admins can create"""

	#Title of the blog
	title = models.CharField(max_length = 100)

	#The author of the blog, but it is not required to have one 
	author = models.CharField(max_length = 100, blank = True)

	#The date when the blog was published
	pub_date = models.DateField()

	#The text field will have unlimited amount of words
	text = models.TextField()

	#The first field for the link which can be blank
	link1 = models.URLField(max_length = 200, blank = True)

	#The second field for link which can be blank
	link2 = models.URLField(max_length = 200, blank = True)

	def __str__(self):
		"""fucntion to return the title of the article on the admin page"""

		return self.title

class Comment(models.Model):
	"""this class will contain all the comments which can be left by users and website visitors under each blog"""

	#many to 1 relatinship
	blog = models.ForeignKey(Blogs, related_name = "comments" ,on_delete = models.CASCADE)

	#name of the author which he or she don't have to write
	name =  models.CharField(max_length = 150, blank = True)

	#the actual comment
	comment = models.TextField()

	def __str__(self):
		"""function to return the name of contents of the comment"""
		return self.comment