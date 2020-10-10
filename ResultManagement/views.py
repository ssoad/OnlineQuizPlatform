import urllib

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import matplotlib.pyplot as plt

from Accounts.models import Examinee
from .models import Result, ExamineeHistory, Rank
import io
import base64
# Create your views here.
@login_required
def showResults(request):
    examinee = Examinee.objects.filter(user=request.user)
    if examinee:
        result = Result.objects.filter(examinee=examinee[0])
    else:
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


@login_required
def showGraph(request, exam_id):
    results = Result.objects.filter(exam_id=exam_id)
    testScore = []
    for result in results:
        testScore.append(int(result.marks))
    bins = [10,20,30, 40, 50, 60, 70, 80, 90, 100]
    plt.hist(testScore, bins, histtype='bar', rwidth=0.8)
    buf = io.BytesIO()
    fig=plt.gcf()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url = urllib.parse.quote(string)
    return render(request,'ResultManagement/analyse.html',context={'data':url})