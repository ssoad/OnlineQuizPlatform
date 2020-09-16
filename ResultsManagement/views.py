from django.shortcuts import render

from .models import Result, ExamineeHistory


# Create your views here.
def showResults(request):
    result = Result.objects.all()
    context = {
        'results': result
    }
    return render(request, 'ResultManagement/Results.html', context)


def showExaminee_History(request):
    history = ExamineeHistory.objects.all()
    context = {
        'ExamineeHistory': history
    }
    return render(request, 'ResultManagement/ExamineeHistory.html', context)
