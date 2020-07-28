from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    # TODO a user may not follow him/her self
    # followers = models.ManyToManyField('self',
    #                                    related_name="followers",
    #                                    symmetrical=False)


class Post(models.Model):
    """Post written by a User."""
    POST_LIMIT = 240
    content = models.CharField(max_length=POST_LIMIT)
    # comments =

# - [ ] *All Posts*: The “All Posts” link in the navigation bar should
#   take the user to a page where they can see all posts from all users,
#   with the most recent posts first.

#   - [ ] Each post should include the username of the poster, the post
#     content itself, the date and time at which the post was made, and
#     the number of “likes” the post has (this will be 0 for all posts
#     until you implement the ability to “like” a post later).
