from django.shortcuts import render
#from django.http import HttpResponse

contexto = {
    'texto': 'Ola mundo',
    'title': 'HOme'
}

# Create your views here.
def home(request):
    return render(
        request,
        'home/index.html',
        contexto
    ) 
