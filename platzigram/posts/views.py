from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView


from posts.forms import PostForm
from posts.models import Post

# from django.http import HttpResponse
from datetime import datetime

# Create your views here.

""" SUBSTITUTED BY PostFeedView Class
@login_required
def list_posts(request):
    #List existing posts
    
    posts = Post.objects.all().order_by('-created')

    context = {
        'posts':posts
    }

    return render(request,'posts/feed.html',context)
"""

class PostsFeedView(LoginRequiredMixin,ListView):
    """Return all published posts"""
    template_name='posts/feed.html'
    model= Post
    ordering=('-created')
    paginate_by = 2
    context_object_name= 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.hTml'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


"""
@login_required
def create(request):
    #Create new post view
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    return render(
        request=request,
        template_name='posts/new.html',
        context = {
            'form':form,
            'user':request.user,
            'profile':request.user.profile
        }
    )
"""