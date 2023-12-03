from django.shortcuts import render

from django.http import HttpResponse

from .models import Post
# dummy blogs
blog_posts = [
    {
        'title': 'Introduction to Python Programming',
        'content': 'Python is a versatile programming language...',
        'author': 'John Doe',
        'publication_date': '2023-01-01',
    },
    {
        'title': 'Getting Started with Django',
        'content': 'Django is a high-level web framework for Python...',
        'author': 'Jane Smith',
        'publication_date': '2023-01-05',
    },
    {
        'title': 'Python Tips and Tricks',
        'content': 'Here are some useful Python tips and tricks...',
        'author': 'Bob Johnson',
        'publication_date': '2023-02-10',
    },
    # Add more blog posts as needed
]


# Create your views here.

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')
    
    