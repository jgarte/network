from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.conf import settings

from .models import User, Post
from .forms import PostForm

# TODO - [ ] *New Post*: Users who are signed in should be able to write a new
#        text-based post by filling in text into a text area and then
#        clicking a button to submit the post.


class PostsView(ListView):
    """Shows a form to create a post and lists all the posts."""
    model = Post
    context_object_name = 'posts'
    template_name = 'network/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'network/index.html'  # for error messages

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AllPostsView(View):
    """List all posts."""
    def get(self, request, *args, **kwargs):
        view = PostsView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CreatePost.as_view()
        return view(request, *args, **kwargs)


class ProfileView(ListView):
    template_name = "network/profile.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        self.user_profile = get_object_or_404(User,
                                              username=self.kwargs['username'])
        return Post.objects.filter(
            author=self.user_profile).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = self.user_profile
        return context


class FollowingView(LoginRequiredMixin, ListView):
    template_name = "network/following.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(
            author__in=self.request.user.following.all())


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("posts"))
        else:
            return render(request, "network/login.html",
                          {"message": "Invalid username and/or password."})
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("posts"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html",
                          {"message": "Passwords must match."})

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html",
                          {"message": "Username already taken."})
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
