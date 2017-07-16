from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def index_view(request):
    return render(request, 'home/index.html', {})


def thinkings(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home/thinkings.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'home/post_detail.html', {'post': post})


def about(request):
    return render(request, 'home/about.html', {})


def contact(request):
    return render(request, 'home/contact.html', {})
