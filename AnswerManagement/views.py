from django.shortcuts import render
from .models import Answer,ExamineeCustomAnswer,ExamineeMCQAnswer

# Create your views here.

def showAnswer(request):

    answer = Answer.objects.all()

    context = {
        'all_answer' : answer
    }

    return render(request, 'AnswerManagement/showAnswer.html',context)


def showMcqAnswer(request):

    Mcqanswer = ExamineeMCQAnswer.objects.all()

    context = {
        'all_mcqanswer' : Mcqanswer
    }

    return render(request, 'AnswerManagement/showMcqAnswer.html')


def showCustomAnswer(request):

    Customanswer = ExamineeCustomAnswer.objects.all()

    context = {
        'all_customanswer' : Customanswer
    }

    return render(request, 'AnswerManagement/showCustomAnswer.html', context)

