from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    context = {
        'title': 'My Website',
        'greeting': 'Hello!',
    }
    

    return render(request, 'index.html', context)

def subscribe(request):
    #return HttpResponse('<div style="color:blue">Subscribed</div>')
    return render(request,'partial.html', {})
