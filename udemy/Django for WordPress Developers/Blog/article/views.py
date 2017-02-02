from django.shortcuts import render

# Create your views here.

def home(request):
    """
    `templates` folder should be manually created within the application
    It will automatically load the htmls from this folder
    """
    return render(request, 'pages/home.html')
