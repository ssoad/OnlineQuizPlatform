from django.shortcuts import render
from .models import Answer, ExamineeAnswer, ExamineeMCQAnswer
from .forms import InsertAnswerForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def showAnswer(request):
    answer = Answer.objects.all()

    context = {
        'all_answer': answer
    }

    return render(request, 'AnswerManagement/showAnswer.html', context)


@login_required
def showMcqAnswer(request):
    Mcqanswer = ExamineeMCQAnswer.objects.all()

    context = {
        'all_mcqanswer': Mcqanswer
    }

    return render(request, 'AnswerManagement/showMcqAnswer.html')


@login_required
def showCustomAnswer(request):
    Customanswer = ExamineeAnswer.objects.all()

    context = {
        'all_customanswer': Customanswer
    }

    return render(request, 'AnswerManagement/showCustomAnswer.html', context)


@login_required
def insertAnswer(request):
    form = InsertAnswerForm()
    message = "Insert Answer"
    if request.method == "POST":
        form = InsertAnswerForm(request.POST)
        message = "Insert Unsuccessful"
        if form.is_valid():
            form.save()
            form = InsertAnswerForm()
            message = "Insert Completed"

    context = {
        'form': form,
        'message': message

    }

    return render(request, 'AnswerManagement/insertAnswer.html', context)
