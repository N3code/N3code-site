from django.shortcuts import render

#packages needed for exporting the fiels as pdf
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def dannilPage(request):
	"""Rendering Daniil's page"""

	return render(request, 'daniil.html')


def exportCertificate(request):
	"""Upon click of the html
	elemnt a certificate will
	be exported as a pdf"""

	# Create a file-like buffer to receive PDF data.
	buffer = io.BytesIO()

	# Create the PDF object, using the buffer as its "file."
	p = canvas.Canvas(buffer)

	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	p.drawString(100, 100, "Hello world.")

	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()

	# FileResponse sets the Content-Disposition header so that browsers
	# present the option to save the file.
	buffer.seek(0)
	return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
	#https://linuxhint.com/download-the-file-in-django/
