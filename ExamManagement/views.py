from django.shortcuts import render

from .models import Exam,AttemptedExam,Question,CustomQuestion,MCQQuestion


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

    questions = Question.objects.all()

    context={
        'all_questions' : questions
    }

    return render(request, 'ExamManagement/showQuestion.html',context)


def showMCQQuestions(request):

    MCQquestions = MCQQuestion.objects.all()

    context = {
        'all_mcqquestions' : MCQquestions
    }

    return render(request, 'ExamManagement/showMCQQuestions.html',context)


def showCustomQuestions(request):

    customquestion = CustomQuestion.objects.all()

    context = {
        'all_customquestions' : customquestion
    }

    return render(request, 'ExamManagement/showCustomQuestion.html',context)




