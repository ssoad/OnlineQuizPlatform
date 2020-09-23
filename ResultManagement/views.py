from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Result, ExamineeHistory, Rank


# Create your views here.
@login_required
def showResults(request):
    result = Result.objects.all()
    context = {
        'results': result
    }
    return render(request, 'ResultManagement/Results.html', context)


@login_required
def showExaminee_History(request):
    history = ExamineeHistory.objects.all()
    context = {
        'ExamineeHistory': history
    }
    return render(request, 'ResultManagement/ExamineeHistory.html', context)


@login_required
def showRank(request):
    rank = Rank.objects.all()
    context = {
        'rank': rank
    }
    return render(request, 'ResultManagement/Rank.html', context)
