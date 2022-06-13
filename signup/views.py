from django.contrib import messages
from .utils import user_exist
from django.shortcuts import render, redirect
from .utils import valid_username
from .forms import UserForm

def signup_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() and valid_username(form):
            form.save()
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request, 'signup/signup.html', context)

def signin_page(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if user_exist(form):
                messages.add_message(request, messages.INFO, 'Logged in!')
                return redirect('home')
    context = {
        'form' : form
    }
    return render(request, 'signup/signin.html', context)



