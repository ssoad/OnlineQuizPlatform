from django.shortcuts import render, redirect
from Accounts.models import Examiner, Examinee
from AnswerManagement.forms import InsertAnswerForm
from AnswerManagement.models import ExamineeAnswer
from ResultManagement.forms import ResultForm
from .forms import AddExamForm, AddMCQquestionform, AddQuestionForm, AddCustomQuestionForm, JoinExam, SearchExam
from .models import Exam, AttemptedExam, Question, CustomQuestion, MCQQuestion
from django.contrib.auth.decorators import login_required
from ResultManagement.models import Result


# Create your views here.
@login_required
def showExams(request, exam_id):
    examinee = Examinee.objects.filter(user=request.user)
    examiner = Examiner.objects.filter(user=request.user)
    form = InsertAnswerForm()
    if examinee:
        if request.method == 'POST':
            form = InsertAnswerForm(request.POST, request.FILES)
            e_id = request.POST.get('exam_id')
            exam = Exam.objects.filter(id=e_id).order_by('-exam_date_time')
            # instance = ExamineeCustomAnswer(exam=exam, examinee=examinee, )
            if form.is_valid():
                answer = form.save(commit=False)
                answer.exam = exam[0]
                answer.examinee = examinee[0]
                answer.checkLate()
                answer.save()
                AttemptedExam.objects.filter(examinee=examinee[0], exam=exam[0]).update(submit=True)
        exams = AttemptedExam.objects.filter(exam_id=exam_id, examinee__user=request.user)
        context = {
            'form': form,
            'examinee': True,
            'exams': exams[0]
        }
    elif examiner:
        exams = Exam.objects.filter(id=exam_id, examiner__user=request.user)
        context = {
            'examiner': True,
            'exams': exams[0]
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
        done = False
        is_Post = False
        message = "Exam was successfully created"
        examiner = Examiner.objects.filter(user_id=request.user.id)
        # print('TEST:',examiner[0])
        if examiner:
            form = AddExamForm(request.POST, request.FILES)
            if request.method == 'POST':
                is_Post = True
                if form.is_valid():
                    exam = form.save(commit=False)
                    exam.save()
                    done = True
                    # form = AddExamForm()
                    # context = {
                    #     'done':True,
                    #     'message': "Exam was successfully created",
                    #     'examiner': True,
                    #     'form': form
                    # }
                    # return render(request, 'ExamManagement/addExam.html', context)
                else:
                    done = False
                    message = "Exam creation failed. Exam Code already exist"
                    # form = AddExamForm()
                    # context = {
                    #     'done': False,
                    #     'message': "Exam creation failed. Exam Code already exist",
                    #     'examiner': True,
                    #     'form': form
                    # }
                    # return render(request, 'ExamManagement/addExam.html', context)

            form = AddExamForm()
            if is_Post:
                context = {
                    'done': done,
                    'message': message,
                    'examiner': True,
                    'form': form
                }
            else:
                context = {
                    # 'done': done,
                    # 'message': message,
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
        # print(request.GET.get('exam_title'))
        if title:
            if examinee:
                exams = AttemptedExam.objects.filter(examinee__user_id=request.user.id,
                                                     exam__exam_title__contains=title)
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
        if examinee:
            form = InsertAnswerForm(request.POST, request.FILES)
            e_id = request.POST.get('exam_id')
            exam = Exam.objects.filter(id=e_id).order_by('-exam_date_time')
            # instance = ExamineeCustomAnswer(exam=exam, examinee=examinee, )
            if form.is_valid():
                answer = form.save(commit=False)
                answer.exam = exam[0]
                answer.examinee = examinee[0]
                answer.checkLate()
                answer.save()
                AttemptedExam.objects.filter(examinee=examinee[0], exam=exam[0]).update(submit=True)
        if examiner:
            del_exam = request.POST.get('del_exam_id')
            if del_exam:
                print(del_exam)
                exam = Exam.objects.get(id=int(del_exam))
                exam.delete()
    if examinee:
        exams = AttemptedExam.objects.filter(examinee__user_id=request.user.id).order_by('-exam__exam_date_time')
        # print(exams[0].exam.exam_title)
        context = {
            'exam': exams,
            'examinee': True,
            'form': form,
            'form2': form2
        }
    else:
        exams = Exam.objects.filter(examiner__user_id=request.user.id).order_by('-exam_date_time')
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
    message = " "
    if request.method == 'POST':
        message = "Join Failed. No Such Exam"
        # print(request.POST.get('exam_code'))
        e_code = int(request.POST.get('exam_code'))
        exam = Exam.objects.filter(exam_code=e_code)
        examinee = Examinee.objects.filter(user=request.user)

        if exam:
            instance = AttemptedExam(exam=exam[0], examinee=examinee[0])
            instance.save()
            message = "Successful"
            context = {
                'form': form,
                'message': message,
                'notfound': False
            }
        else:
            context = {
                'form': form,
                'message': message,
                'notfound': True
            }

        return render(request, 'ExamManagement/join_exam.html', context)
    context = {
        'form': form,
    }
    return render(request, 'ExamManagement/join_exam.html', context)


@login_required
def individual_result(request, exam_id):
    result = Result.objects.filter(exam=exam_id, examinee__user=request.user)
    exam = Exam.objects.filter(id=exam_id)
    print(len(result))
    if len(result) == 0:
        context = {
            'message': 'Result Not Published'
        }
        return render(request, 'Failed.html', context)
    context = {
        'result': result[0],
        'exam': exam[0]
    }
    return render(request, 'ResultManagement/IndivResult.html', context)


def exam_result(request, exam_id):
    result = Result.objects.filter(exam=exam_id)
    exam = Exam.objects.filter(id=exam_id)
    title = request.GET.get('exam_title')
    if request.method == 'GET' and title:
        form = SearchExam(request.GET)
        if form.is_valid:
            result1 = Result.objects.filter(exam__exam_title__contains=title, exam_id=exam_id)
            result2 = Result.objects.filter(examinee__user__first_name__contains=title, exam_id=exam_id)
            result3 = Result.objects.filter(examinee__user__last_name__contains=title, exam_id=exam_id)
            result = result1 | result2 | result3
    form = SearchExam()
    context = {
        'form': form,
        'examiner': True,
        'result': result,
        'exam': exam[0]
    }
    return render(request, 'ResultManagement/ExamResult.html', context)


def showHome(request):
    if request.user.is_authenticated:
        examinee = Examinee.objects.filter(user=request.user)
        examiner = Examiner.objects.filter(user=request.user)
        if examinee:
            context = {
                'examinee': True
            }
            return render(request, 'Index.html', context)
        elif examiner:
            context = {
                'examiner': True
            }
            return render(request, 'Index.html', context)
    return render(request, 'Index.html')


def contact_us(request):
    return render(request, 'contactus.html')


def showSubmissions(request, exam_id):
    # examinee = Examinee.objects.filter(user=request.user)
    examiner = Examiner.objects.filter(user=request.user)
    # form = InsertAnswerForm()
    form2 = SearchExam()
    if examiner:
        if request.method == 'POST':
            examinee_id = request.POST.get('examinee_id')
            form = ResultForm(request.POST, request.FILES)
            exam_ = Exam.objects.filter(id=exam_id)
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
                ExamineeAnswer.objects.filter(examinee=examinee_[0], exam=exam_[0]).update(graded=True)
                answers = ExamineeAnswer.objects.filter(exam_id=exam_[0].id)

                context = {
                    'examiner': True,
                    'answers': answers,
                    'form': form,
                    'form2': form2
                }
                return render(request, 'ExamManagement/showSubmission.html', context)
        form = ResultForm()
        # print(request.POST.get('exam_id'))
        answers = ExamineeAnswer.objects.filter(exam_id=exam_id)

        context = {
            'examiner': True,
            'answers': answers,
            'form': form,
            'form2': form2
        }
        return render(request, 'ExamManagement/showSubmission.html', context)
    else:
        return render(request, 'Failed.html', {'message': "You're Not Allowed Here"})


def exam_ranks(request, exam_id):
    result = Result.objects.filter(exam=exam_id).order_by('-marks')
    exam = Exam.objects.filter(id=exam_id)
    form = SearchExam()
    context = {
        'form': form,
        'result': result,
        'exam': exam[0]
    }
    return render(request, 'ResultManagement/ExamRank.html', context)


def allresults(request):
    result = Result.objects.filter(exam__examiner__user__id=request.user.id)
    title = request.GET.get('exam_title')
    if request.method == 'GET' and title:
        form = SearchExam(request.GET)
        if form.is_valid:
            result1 = Result.objects.filter(exam__exam_title__contains=title, exam__examiner__user__id=request.user.id)
            result2 = Result.objects.filter(examinee__user__first_name__contains=title,
                                            exam__examiner__user__id=request.user.id)
            result3 = Result.objects.filter(examinee__user__last_name__contains=title,
                                            exam__examiner__user__id=request.user.id)
            result = result1 | result2 | result3
    form = SearchExam()
    context = {
        'form': form,
        'examiner': True,
        'result': result,
        # 'exam': exam[0]
    }
    return render(request, 'ResultManagement/Results.html', context)


def showParticipant(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    participant = AttemptedExam.objects.filter(exam_id=exam_id)
    context = {
        'participant': participant,
        'exam': exam
    }
    return render(request, 'ExamManagement/show_participant.html', context)
