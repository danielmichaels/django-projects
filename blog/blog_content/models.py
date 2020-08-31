from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    Blog post model
    """

    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
