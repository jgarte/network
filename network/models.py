from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse


class User(AbstractUser):
    pass
    # TODO a user may not follow him/her self
    # Validators ^?
    # followers = models.ManyToManyField('self',
    #                                    related_name="followers",
    #                                    symmetrical=False)


class Post(models.Model):
    """
    Each post should include the username of the poster, the post
    content itself, the date and time at which the post was made, and
    the number of “likes” the post has (this will be 0 for all posts
    until you implement the ability to “like” a post later).
    """
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

    def __str__(self):
        return f"Author: {self.author}"

    def get_absolute_url(self):
        return reverse('posts')
