from django.shortcuts import render

# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse


def dannilPage(request):
	"""Rendering Daniil's page"""

	return render(request, 'daniil.html')



# Define function to download pdf file using template
def download_pdf_file(request):
	# Define Django project base directory
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	filename = 'cert-1073-9082354.pdf'
	# Define the full file path
	filepath = BASE_DIR + '/static/' + filename
	# Open the file for reading content
	path = open(filepath, 'rb')
	# Set the mime type
	mime_type, _ = mimetypes.guess_type(filepath)
	# Set the return value of the HttpResponse
	response = HttpResponse(path, content_type=mime_type)
	# Set the HTTP header for sending to browser
	response['Content-Disposition'] = "attachment; filename=%s" % filename
	# Return the response value
	return response
    