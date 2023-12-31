from django.shortcuts import render
from blog.data import posts

# Create your views here.
def blog(request):

    contexto = {
        'texto': 'Meu blog',
        'title': 'Blog',
        'posts': posts
    }
    
    return render(
        request,
        'blog/index.html',
        contexto
    ) 

def post(request, id):

    print('post', id)

    contexto = {
        'posts': posts,
        'title': 'Blog',
    }
    
    return render(
        request,
        'blog/index.html',
        contexto
    ) 