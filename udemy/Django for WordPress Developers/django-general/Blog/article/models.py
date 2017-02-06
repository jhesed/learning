"""
Creates a data store model for the Post class
Author: Jhesed D. Tacadena
Date: 2017-02-02
"""

from django.db import models
from django.utils import timezone

# -----------------------------------------------------------------------------
class Post(models.Model):
    """
    Defines the Post model class
    """

    author = models.ForeignKey('auth.User')  # Pulls user names from User table
    title = models.CharField(max_length=150, null=False)
    text = models.TextField(null=False)
    created_date = models.DateTimeField(default=timezone.now)
    # move this to /media etc. in the future
    image = models.FileField(blank=True, upload_to='images')

    # Add a many to many database filed
    category = models.ManyToManyField('article.Category', 
        blank=True, null=True)  

    # -------------------------------------------------------------------------
    def __str__(self):
        """
        This will allow Django admin to return the title instead
        of the "Post object" string
        """
        return self.title

# -------------------------------------------------------------------------
class Category(models.Model):
    """
    Defined the Category model class
    """

    title = models.CharField(max_length=150)    
    slug = models.CharField(max_length=150)    
    # Allow Category to have a parent category
    parent = models.ForeignKey('article.Category', blank=True, null=True)
    
    # -------------------------------------------------------------------------
    def __str__(self):
        """
        This will allow Django admin to return the title instead
        of the "Post object" string
        """
        return self.title

    # -------------------------------------------------------------------------
    @staticmethod
    def list_categories():
        """
        Return list of categoreis
        """
        return Category.objects.all()

    