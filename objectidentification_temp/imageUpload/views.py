from django.shortcuts import render

# Create your views here.
def upload_image(request):
    return render(request, 'uploadimage.html')