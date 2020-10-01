from django.shortcuts import render
from Accounts.models import Examinee, Examiner
import django.contrib.staticfiles


# Create your views here.
def showHome(request):
    if request.user.is_authenticated:
        examinee = Examinee.objects.filter(user=request.user)
        examiner = Examiner.objects.filter(user=request.user)
        if examinee:
            context = {
                'examinee': True
            }
            return render(request, 'Index.html', context)
        elif examiner:
            context = {
                'examiner': True
            }
            return render(request, 'Index.html', context)
    return render(request, 'Index.html')


def contact_us(request):
    return render(request, 'contactus.html')
