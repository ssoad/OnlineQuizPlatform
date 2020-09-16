from django.shortcuts import render
from .models import Answer,ExamineeCustomAnswer,ExamineeMCQAnswer

# Create your views here.

def showAnswer(request):

    answer = Answer.objects.all()

    context = {
        'all_answer' : answer
    }

    return render(request, 'AnswerManagement/showAnswer.html',context)
