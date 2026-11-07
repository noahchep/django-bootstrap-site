from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def home(request):
    return render(request, 'index.html')


def resume(request):
    return render(request, 'resume.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})