from django.shortcuts import render
from article.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


# -----------------------------------------------------------------------------
def home(request):
    """
    `templates` folder should be manually created within the application
    It will automatically load the htmls from this folder
    
    """

    # Fetch every object from Post Model
    post_list = Post.objects.all()

    # paginate on the second parameter. i.e. 
    # value of 2 will paginate every 2 posts
    paginator = Paginator(post_list, 1)

    # `page` is embedded automatically by Paginator class
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    
    except PageNotAnInteger:  
        # Django.Paginator custom exception
        # Set post to something else
        posts = paginator.page(1)

    except EmptyPage:
        # Django.Paginator custom exception
        # load the last page
        posts = paginator.page(paginator.num_pages)

    return render(request, 'pages/home.html', {'posts': posts})

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
 