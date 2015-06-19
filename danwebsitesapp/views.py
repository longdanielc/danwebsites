from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'danwebsitesapp/index.htm')

def events(request):
    return HttpResponse("Events!")

def testimonials(request):
    return render(request, 'danwebsitesapp/testimonials.htm')

def contact(request):
    return render(request, 'danwebsitesapp/contact.htm')
