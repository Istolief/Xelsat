from django.shortcuts import render, get_object_or_404
from .models import Post
# from django.utils import timezone


def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter().order_by('published_date')
    return render(request, 'news/post_list.html', {'posts': posts, 'category': get_category()})


def events_list(request):
    posts = Post.objects.filter(event=True).order_by('published_date')
    return render(request, 'news/post_list.html', {'posts': posts, 'category': get_category()})


def news_list(request):
    posts = Post.objects.filter(news=True).order_by('published_date')
    return render(request, 'news/post_list.html', {'posts': posts, 'category': get_category()})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # return render(request, 'news/post_detail.html', {'post': post})
    return render(request, 'news/post_list.html', {'posts': [post], 'category': get_category()})


def get_category():
    return {
        'news': Post.objects.filter(news=True).count(),
        'events': Post.objects.filter(event=True).count(),
    }
