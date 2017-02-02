from django.shortcuts import render
from article.models import Post

# Create your views here.


# -----------------------------------------------------------------------------
def home(request, username):
    """
    `templates` folder should be manually created within the application
    It will automatically load the htmls from this folder
    
    Argument:
        username (str): Name of the user from the User table

    """

    # Fetch every object from Post Model
    posts = Post.objects.all()
    
    context = {
        'posts': posts,
        'current_user': username
    }

    return render(request, 'pages/home.html', context)

# ----------------------------------------------------------------------------- 
def single(request, single):
    """
    View for rendering page for single posts

    `templates` folder should be manually created within the application
    It will automatically load the htmls from this folder
    
    Argument:
        single (str): 
    """

    # Retrieve a single post based from parameter single
    single = Post.objects.get(id=single)

    context = {
        'post': single,
    }

    return render(request, 'pages/single.html', context)
 