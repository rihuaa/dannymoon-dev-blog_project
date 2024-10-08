from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.


def index(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	return render(request, 'blog/index.html', {'posts':posts})

def topics(request, pk):
	posts = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/topics.html', {'posts':posts})

def about(request):
	return render(request, 'blog/about.html', {})

def contact(request):
	return render(request, 'blog/contact.html', {})

