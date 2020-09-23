from django.shortcuts import render
from .models import Answer, ExamineeCustomAnswer, ExamineeMCQAnswer
from .forms import insertAnswerform
from django.contrib.auth.decorators import login_required


# Create your views here.

def showAnswer(request):
    answer = Answer.objects.all()

    context = {
        'all_answer': answer
    }

    return render(request, 'AnswerManagement/showAnswer.html', context)


def showMcqAnswer(request):
    Mcqanswer = ExamineeMCQAnswer.objects.all()

    context = {
        'all_mcqanswer': Mcqanswer
    }

    return render(request, 'AnswerManagement/showMcqAnswer.html')


def showCustomAnswer(request):
    Customanswer = ExamineeCustomAnswer.objects.all()

    context = {
        'all_customanswer': Customanswer
    }

    return render(request, 'AnswerManagement/showCustomAnswer.html', context)


@login_required
def insertAnswer(request):
    form = insertAnswerform()
    message = "Insert Answer"
    if request.method == "POST":
        form = insertAnswerform(request.POST)
        message = "Insert Unsuccessful"
        if form.is_valid():
            form.save()
            form = insertAnswerform()
            message = "Insert Completed"

    context = {
        'form': form,
        'message': message

    }

    return render(request, 'AnswerManagement/insertAnswer.html', context)
