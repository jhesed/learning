"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings  # gives access to settings.py
from django.views import static as django_static

from article import views as article_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', article_view.home),
    url(r'post/(?P<single>[-\w]+)/$', article_view.single, name='single'),
    url(r'category/(?P<category>[-\w]+)/$', article_view.archive, name='category'),

    # images folder, absolute path directory is necessary. 
    # special django command; settings.base_dir ust
    url(r'images/(?P<path>.*)/$', django_static.serve, 
        {'document_root': settings.BASE_DIR + '/images'}),

]
