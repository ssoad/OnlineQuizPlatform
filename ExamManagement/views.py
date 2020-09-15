from django.shortcuts import render
from .models import Exam
# Create your views here.

def showExams(request):

    exams = Exam.objects.all()

    context={
        'all_exams': exams
    }

    return render(request, 'ExamManagement/showExam.html',context)

