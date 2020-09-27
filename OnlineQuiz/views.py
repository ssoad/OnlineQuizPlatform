from django.shortcuts import render
import django.contrib.staticfiles

# Create your views here.
def showHome(request):
    return render(request, 'Index.html')


def contact_us(request):
    return render(request, 'contactus.html')