from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts=Post.objects.all()   # here posts is a list (iterable) conataining objects
    return render(request, 'index.html', {'posts':posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)  # here posts variable is not an iterable its just a single value containing the id of the particular object.
    # and from that id we will be able to access the attributes of that object in the posts.html file.
    return render(request, 'posts.html', {'posts': posts})
