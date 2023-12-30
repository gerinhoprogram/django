from django.shortcuts import render

contexto = {
    'texto': 'Ola mundo',
    'title': 'HOme'
}

# Create your views here.
def blog(request):
    return render(
        request,
        'blog/index.html',
        contexto
    ) 