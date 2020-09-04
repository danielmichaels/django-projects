from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    """
    Blog post model
    """

    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """
        In CBV, the redirect chain on a form submit needs this, else
        it can't redirect.
        """
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
