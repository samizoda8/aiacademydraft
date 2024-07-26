from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def basiccourse(request):
    return render(request, 'home/basiccourse.html')


def dataanalytics(request):
    return render(request, 'home/dataanalytics.html')

def datascience(request):
    return render(request, 'home/datascience.html')

def contact(request):
    return render(request, 'home/contact.html')


def courses(request):
    return render(request, 'home/courses.html')
