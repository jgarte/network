from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse


class User(AbstractUser):
    following = models.ManyToManyField('self',
                                       related_name="followers",
                                       symmetrical=False)


class Post(models.Model):
    POST_LIMIT = 240
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    content = models.CharField(max_length=POST_LIMIT)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,
                                   related_name="likes",
                                   related_query_name="like",
                                   blank=True)
    # TODO comments

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"Author: {self.author}"

    def get_absolute_url(self):
        return reverse('posts')
