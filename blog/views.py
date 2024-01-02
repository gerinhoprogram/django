from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404

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

def post(request: HttpRequest, post_id: int):

    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('post não encontrado')

    contexto = {
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }
    
    return render(
        request,
        'blog/post.html',
        contexto
    ) 