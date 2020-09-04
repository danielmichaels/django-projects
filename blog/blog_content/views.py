from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog_content.models import Post


class PostListView(ListView):
    """
    CBV PostList

    CBV templates: <app>/<model>_<viewtype>.html | 'blog_content/post_list.html
    """

    model = Post
    template_name = "blog_content/home.html"  # else 'post_list.html'
    context_object_name = "posts"  # else it looks for 'object_list' instead of post
    ordering = ["-date_posted"]
    paginate_by = 2


class PostDetailView(DetailView):
    """
    Each posts detailed view
    """

    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    User can write a post in browser
    """

    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        """
        override the CBV to include author.id
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    User can update a post in browser
    """

    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        """
        override the CBV to include author.id
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Must declare this if using UserPassesTestMixin

        Here we make sure only author can update their posts.
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Each posts detailed view
    """

    model = Post
    success_url = "/"

    def test_func(self):
        """
        Must declare this if using UserPassesTestMixin

        Here we make sure only author can update their posts.
        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def home(request):
    posts = Post.objects.all()
    context = {"title": "blogZzZ", "posts": posts}
    return render(request, "blog_content/home.html", context)


def about(request):
    context = {}
    return render(request, "blog_content/about.html", context)
