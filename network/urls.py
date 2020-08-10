
from django.urls import path

from . import views

urlpatterns = [
    path("", views.AllPostsView.as_view(), name="posts"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.FollowingView.as_view(), name='following'),
    path("<username>", views.ProfileView.as_view(), name='profile'),
]
