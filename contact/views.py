from django.shortcuts import render
from .forms import getintouch_form

# Create your views here.

def getintouch_function(request):
    if request.method == 'POST':
        form = getintouch_form(request.POST)
        if form.is_valid():
            form.save()
                
    else:
        form = getintouch_form()

    return render(request, 'contact.html' , {'form': form})    