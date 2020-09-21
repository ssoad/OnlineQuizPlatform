import datetime
from django.shortcuts import render
from Accounts.models import Examiner
from .forms import AddExamForm,AddMCQquestionform
from .models import Exam, AttemptedExam, Question, CustomQuestion, MCQQuestion


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

    return render(request, 'ExamManagement/showAttemptedExam.html', context)


def showQuestions(request):
    questions = Question.objects.all()

    context = {
        'all_questions': questions
    }

    return render(request, 'ExamManagement/showQuestion.html', context)


def showMCQQuestions(request):
    MCQquestions = MCQQuestion.objects.all()

    context = {
        'all_mcqquestions': MCQquestions
    }

    return render(request, 'ExamManagement/showMCQQuestions.html', context)


def showCustomQuestions(request):
    customquestion = CustomQuestion.objects.all()

    context = {
        'all_customquestions': customquestion
    }

    return render(request, 'ExamManagement/showCustomQuestion.html', context)


def addExam(request):
    if request.user.is_authenticated:
        examiner = Examiner.objects.filter(user_id=request.user.id)

        #print('TEST:',examiner[0])
        if examiner:
            form = AddExamForm(request.POST or None)
            if request.method == 'POST':
                if form.is_valid():
                    # form.save()
                    title = form.cleaned_data.get('exam_title')
                    code = int(form.cleaned_data.get('exam_code'))
                    marks = int(form.cleaned_data.get('exam_marks'))
                    date_time = datetime.datetime.now() #For Testing purpose
                    duration = int(form.cleaned_data.get('exam_duration'))
                    exam = Exam(exam_title=title, examiner=examiner[0], exam_code=code, exam_marks=marks, exam_duration=duration, exam_date_time=date_time)
                    exam.save()
                    form = AddExamForm()
            context = {
                'form': form
            }
            return render(request, 'ExamManagement/addExam.html', context)
        else:
            return render(request, '404.html')
    return render(request, '404.html')


def insertMcqQuestion(request):

    form = AddMCQquestionform()
    message = "Insert Question"
    if request.method == "POST":
        form = AddMCQquestionform(request.POST)
        message = "Not Successful"
        if form.is_valid():
            form.save()
            form = AddMCQquestionform()
            message = "Successful"

    context = {
        'form' : form,
        'message' : message
    }

    return render(request,'ExamManagement/insertMcqQuestionform.html',context)