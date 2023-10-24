from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import Signup_form

# Create your views here.

def signup_function(request):
    if request.method == 'POST':
       form = Signup_form(request.POST)
       if form.is_valid():
          form.save()
          
                
    else:
        form = Signup_form()


    return render(request, 'signup.html', {'form': form})