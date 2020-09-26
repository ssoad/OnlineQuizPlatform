import datetime
from django.shortcuts import render
from Accounts.models import Examiner, Examinee
from .forms import AddExamForm, AddMCQquestionform, AddQuestionForm, AddCustomQuestionForm
from .models import Exam, AttemptedExam, Question, CustomQuestion, MCQQuestion
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def showExams(request):
    exams = Exam.objects.filter(examiner__user_id=request.user.id)

    context = {
        'examiner': True,
        'all_exams': exams
    }

    return render(request, 'ExamManagement/showExam.html', context)


@login_required
def showAttemptedExam(request):
    att_exams = AttemptedExam.objects.all()

    context = {
        'all_att_exams': att_exams
    }

    return render(request, 'ExamManagement/showAttemptedExam.html', context)


@login_required
def showQuestions(request):
    questions = Question.objects.all()

    context = {
        'all_questions': questions
    }

    return render(request, 'ExamManagement/showQuestion.html', context)


@login_required
def showMCQQuestions(request):
    MCQquestions = MCQQuestion.objects.all()

    context = {
        'all_mcqquestions': MCQquestions
    }

    return render(request, 'ExamManagement/showMCQQuestions.html', context)


@login_required
def showCustomQuestions(request):
    customquestion = CustomQuestion.objects.all()

    context = {
        'all_customquestions': customquestion
    }

    return render(request, 'ExamManagement/showCustomQuestion.html', context)


@login_required
def addExam(request):
    if request.user.is_authenticated:
        examiner = Examiner.objects.filter(user_id=request.user.id)

        # print('TEST:',examiner[0])
        if examiner:
            form = AddExamForm(request.POST or None)
            if request.method == 'POST':
                if form.is_valid():
                    # form.save()
                    title = form.cleaned_data.get('exam_title')
                    code = int(form.cleaned_data.get('exam_code'))
                    marks = int(form.cleaned_data.get('exam_marks'))
                    date_time = datetime.datetime.now()  # For Testing purpose
                    duration = int(form.cleaned_data.get('exam_duration'))
                    exam = Exam(exam_title=title, examiner=examiner[0], exam_code=code, exam_marks=marks,
                                exam_duration=duration, exam_date_time=date_time)
                    exam.save()
                    form = AddExamForm()
            context = {
                'examiner': True,
                'form': form
            }
            return render(request, 'ExamManagement/addExam.html', context)
        else:
            return render(request, '404.html')
    return render(request, '404.html')


@login_required
def insertMcqQuestion(request):
    if request.user.is_authenticated:
        examiner = Examiner.objects.filter(user_id=request.user.id)

        # print('TEST:',examiner[0])
        if examiner:
            form = AddMCQquestionform()
            message = "Insert Question"
            if request.method == "POST":
                form = AddMCQquestionform(request.POST)
                message = "Insert Unsuccessful"
                if form.is_valid():
                    form.save()
                    form = AddMCQquestionform()
                    message = "Insert Completed"

            context = {
                'form': form,
                'message': message
            }

            return render(request, 'ExamManagement/insertMcqQuestionform.html', context)
        else:
            return render(request, '404.html')
    return render(request, '404.html')


@login_required
def AddQuestion(request):
    examiner = Examiner.objects.filter(user_id=request.user.id)

    # print('TEST:',examiner[0])
    if examiner:
        addqus = AddQuestionForm()
        context = {
            'Question': addqus
        }
        return render(request, 'ExamManagement/addQuestion.html', context)
    else:
        return render(request, '404.html')


@login_required
def AddCustomQuestion(request):
    examiner = Examiner.objects.filter(user_id=request.user.id)

    # print('TEST:',examiner[0])
    if examiner:
        addcus_qus = AddCustomQuestionForm()
        context = {
            'CustomQuestion': addcus_qus
        }
        return render(request, 'ExamManagement/addCustomQuestion.html', context)
    else:
        return render(request, '404.html')


@login_required
def ExamHistory(request):
    examinee = Examinee.objects.filter(user=request.user)
    # examiner = Examiner.objects.filter(user=request.user)
    if examinee:
        exams = AttemptedExam.objects.filter(examinee__user_id=request.user.id)
        #print(exams[0].exam.exam_title)
        context = {
            'exam': exams,
            'examinee': True
        }
    else:
        exams = Exam.objects.filter(examiner__user_id=request.user.id)
        print(exams)
        context = {
            'exam': exams,
            'examiner': True
        }
    return render(request, 'ExamManagement/ExamHistory.html', context)
