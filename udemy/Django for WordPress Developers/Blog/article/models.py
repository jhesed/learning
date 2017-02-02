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
    title = models.CharField(max_length=150, null=True)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    # -------------------------------------------------------------------------
    def __str__(self):
        """
        This will allow Django admin to return the title instead
        of the "Post object" string
        """
        return self.title