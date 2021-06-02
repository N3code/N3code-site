from django.contrib import admin
from .models import Blogs, Comment

# Registered the model so that it will be displayed on the admin page
admin.site.register(Blogs)

#Registered the Comments model so that it will be displayed on the admin page
admin.site.register(Comment)