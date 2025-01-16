from django.http import HttpResponse
from django.shortcuts import render


# Home page
def home(request):
    return render(request, 'index.html')

# About us page
def about(request):
    return render(request, 'about.html')

# Contact us page
def contact(request):
    return render(request, 'contact.html')

# Our Services page
def services(request):
    return render(request, 'services.html')

