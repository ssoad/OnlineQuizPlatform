from django.shortcuts import render

from .models import Exam,AttemptedExam


# Create your views here.

def showExams(request):
    exams = Exam.objects.all()

    context = {
        'all_exams': exams
    }

    return render(request, 'ExamManagement/showExam.html', context)


def showAttemptedExam(request):

    att_exams = AttemptedExam.objects.all()

    context = {
        'all_att_exams': att_exams
    }

    return render(request, 'ExamManagement/showAttemptedExam.html',context)



