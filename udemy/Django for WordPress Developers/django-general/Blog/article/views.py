from django.shortcuts import render
from article.models import Post, Category
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
    categories = Category.list_categories()

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

    return render(request, 'pages/home.html', 
        {'posts': posts, 'categories': categories})

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
 
# ----------------------------------------------------------------------------- 
def archive(request, category):
    """
    View for rendering page for rendering categories

    `templates` folder should be manually created within the application
    It will automatically load the htmls from this folder
    
    Argument:
        category (str): Category slug
    """

    # Fetch posts based on the category
    cat = Category.objects.get(slug=category)
    # __ is special in django. its a direct call in model attributes
    post_list = Post.objects.filter(category__pk=cat.id)

    # paginate on the second parameter. i.e. 
    # value of 2 will paginate every 2 posts
    paginator = Paginator(post_list, 1)

    # `page` is embedded automatically by Paginator class
    page = request.GET.get('page')
    categories = Category.list_categories()

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

    return render(request, 'pages/archive.html', 
        {'posts': posts, 'categories': categories})
