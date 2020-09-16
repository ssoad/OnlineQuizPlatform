from django.shortcuts import render

from .models import Exam,AttemptedExam,Questions,Custom_Questions,MCQ_Questions


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


def showQuestions(request):

    questions = Questions.objects.all()

    context={
        'all_questions' : questions
    }

    return render(request, 'ExamManagement/showQuestion.html',context)


def showMCQQuestions(request):

    MCQquestions = MCQ_Questions.objects.all()

    context = {
        'all_mcqquestions' : MCQquestions
    }

    return render(request, 'ExamManagement/showMCQQuestions.html',context)


def showCustomQuestions(request):

    Customquestions = Custom_Questions.objects.all()

    context = {
        'all_customquestions' : Customquestions
    }

    return render(request, 'ExamManagement/showCustomQuestion.html',context)




