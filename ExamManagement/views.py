import datetime
from django.shortcuts import render
from Accounts.models import Examiner, Examinee
from AnswerManagement.forms import InsertAnswerForm
from AnswerManagement.models import ExamineeCustomAnswer
from ResultManagement.forms import ResultForm
from .forms import AddExamForm, AddMCQquestionform, AddQuestionForm, AddCustomQuestionForm, JoinExam, SearchExam
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
            form = AddExamForm(request.POST, request.FILES)
            if request.method == 'POST':
                if form.is_valid():
                    exam = form.save(commit=False)
                    # title = form.cleaned_data.get('exam_title')
                    # code = int(form.cleaned_data.get('exam_code'))
                    # marks = int(form.cleaned_data.get('exam_marks'))
                    # For Testing purpose
                    # duration = int(form.cleaned_data.get('exam_duration'))
                    # exam = Exam(exam_title=title, examiner=examiner[0], exam_code=code, exam_marks=marks,
                    #             exam_duration=duration, exam_date_time=date_time)
                    # date_time = datetime.datetime.now()
                    # exam.exam_date_time = date_time
                    # print(exam.exam_date_time)
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
    examiner = Examiner.objects.filter(user=request.user)
    form = InsertAnswerForm()
    form2 = SearchExam()
    if request.method == 'GET':
        title = request.GET.get('exam_title')
        #print(request.GET.get('exam_title'))
        if title:
            if examinee:
                exams = AttemptedExam.objects.filter(examinee__user_id=request.user.id,exam__exam_title__contains=title)
                # print(exams[0].exam.exam_title)
                context = {
                    'exam': exams,
                    'examinee': True,
                    'form': form,
                    'form2': form2
                }
                return render(request, 'ExamManagement/ExamHistory.html', context)
            else:
                exams = Exam.objects.filter(examiner__user_id=request.user.id, exam_title__contains=title)
                # print(exams)
                context = {
                    'exam': exams,
                    'examiner': True,
                    'form2': form2
                }
            return render(request, 'ExamManagement/ExamHistory.html', context)

    if request.method == 'POST':
        if examiner:
            e_id = request.POST.get('exam_id')
            exm_id = request.POST.get('exm_id')
            examinee_id = request.POST.get('examinee_id')
            form = ResultForm()
            # print(request.POST.get('exam_id'))
            if e_id:
                answers = ExamineeCustomAnswer.objects.filter(exam_id=e_id)

                context = {
                    'examiner': True,
                    'answers': answers,
                    'form': form,
                    'form2': form2
                }
                return render(request, 'ExamManagement/showSubmission.html', context)
            elif exm_id and examinee_id:
                form = ResultForm(request.POST)
                exam_ = Exam.objects.filter(id=exm_id)
                examinee_ = Examinee.objects.filter(id=examinee_id)
                # answers = ExamineeCustomAnswer.objects.filter(exam_id=e_id)
                # context = {
                #     'answers': answers,
                #     'form': form
                # }
                if form.is_valid:
                    result = form.save(commit=False)
                    result.examinee = examinee_[0]
                    result.exam = exam_[0]
                    # print(result.marks)
                    result.save()
                    # print(form.cleaned_data.get('marks'))
                    ExamineeCustomAnswer.objects.filter(examinee=examinee_[0], exam=exam_[0]).update(marks=True)
                    answers = ExamineeCustomAnswer.objects.filter(exam_id=exam_[0].id)

                    context = {
                        'examiner': True,
                        'answers': answers,
                        'form': form,
                        'form2': form2
                    }
                    return render(request, 'ExamManagement/showSubmission.html', context)
        else:
            form = InsertAnswerForm(request.POST, request.FILES)
            e_id = request.POST.get('exam_id')
            exam = Exam.objects.filter(id=e_id)
            # instance = ExamineeCustomAnswer(exam=exam, examinee=examinee, )
            if form.is_valid():
                answer = form.save(commit=False)
                answer.exam = exam[0]
                answer.examinee = examinee[0]
                answer.save()
                AttemptedExam.objects.filter(examinee=examinee[0], exam=exam[0]).update(submit=True)
    if examinee:
        exams = AttemptedExam.objects.filter(examinee__user_id=request.user.id)
        # print(exams[0].exam.exam_title)
        context = {
            'exam': exams,
            'examinee': True,
            'form': form,
            'form2': form2
        }
    else:
        exams = Exam.objects.filter(examiner__user_id=request.user.id)
        # print(exams)
        context = {
            'exam': exams,
            'examiner': True,
            'form2': form2
        }
    return render(request, 'ExamManagement/ExamHistory.html', context)


@login_required
def joinExam(request):
    form = JoinExam()
    if request.method == 'POST':
        # print(request.POST.get('exam_code'))
        e_code = int(request.POST.get('exam_code'))
        exam = Exam.objects.filter(exam_code=e_code)
        examinee = Examinee.objects.filter(user=request.user)
        instance = AttemptedExam(exam=exam[0], examinee=examinee[0])
        instance.save()
    context = {
        'form': form
    }
    return render(request, 'ExamManagement/join_exam.html', context)
