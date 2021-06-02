from django.shortcuts import render

# Create your views here.

def TanPage(request):
    """Rendering Tan's Page"""

    return render(request, 'Tan.html')