from django.shortcuts import render



def index(request):
    return render(request, 'index.html', {'section': 'index'})

def contact(request):
    return render(request, 'contact.html', {'section': 'contact'})



def about(request):
    return render(request, 'about.html', {'section': 'about'})

def teacher(request):
    return render(request, 'teacher.html', {'section': 'teacher'})

def vehicle(request):
    return render(request, 'vehicle.html', {'section': 'vehicle'})

# Create your views here.
