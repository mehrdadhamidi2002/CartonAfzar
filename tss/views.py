from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm  # Import your ContactForm

def home(request):

    context = {
        'title': 'My Website',
        'greeting': 'Hello!',
    }
    

    return render(request, 'index.html', context)

def subscribe(request):
    #return HttpResponse('<div style="color:blue">Subscribed</div>')
    return render(request,'partial.html', {})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
           # return redirect('/')  # Redirect to a success page
    else:
        form = ContactForm()

    #return render(request, 'contact_form.html', {'form': form})
    return HttpResponse('ok')

