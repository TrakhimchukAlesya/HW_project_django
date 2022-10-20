from django.shortcuts import render
from .models import Blog


def blog_index(request):
    blogs = Blog.objects.order_by('-created_on')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)

# Create your views here.
