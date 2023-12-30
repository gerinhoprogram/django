from django.shortcuts import render
from blog.data import posts

contexto = {
    'texto': 'Meu blog',
    'title': 'Blog',
    'posts': posts
}

# Create your views here.
def blog(request):
    return render(
        request,
        'blog/index.html',
        contexto
    ) 