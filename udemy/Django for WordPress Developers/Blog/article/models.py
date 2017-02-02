"""
Creates a data store model for the Post class
Author: Jhesed D. Tacadena
Date: 2017-02-02
"""

from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    Defines the Post model class
    """

    author = models.ForeignKey('auth.User') 

