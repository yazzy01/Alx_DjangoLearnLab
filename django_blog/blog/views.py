from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from .models import Comment, Post
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "blog/profile.html")



from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/posts/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm(request.POST or None)

    if request.method == 'POST' and request.user.is_authenticated:
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})


class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})


from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Comment, Post
from django.urls import reverse_lazy

class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']  # assuming your Comment model has a content field for the comment text
    template_name = 'blog/comment_form.html'  # Specify your template for creating a comment

    def form_valid(self, form):
        # Set the post for the comment from the URL
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user  # Assuming you want to automatically assign the current user as the author
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the post detail page after successful comment creation
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

