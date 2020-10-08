"""OnlineQuizPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Accounts import views as acc_views
from Accounts.models import Examiner, Examinee
from ExamManagement import views as exam_views
from ResultManagement import views as result_views
from AnswerManagement import views as answer_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', exam_views.showHome),
    path('login/', acc_views.login_view),
    path('signup/', acc_views.register_view),
    path('logout/', acc_views.logout_view),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('reset-password/', auth_views.PasswordResetView.as_view()),
    path('reset-password-confirm/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset-password-done/', auth_views.PasswordResetDoneView.as_view()),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view()),
    path('dashboard/', acc_views.user_dash),
    path('contact/', exam_views.contact_us),
    path('admin/', admin.site.urls),
    path('showexams/<int:exam_id>', exam_views.showExams, name='exams'),
    path('attexams/', exam_views.showAttemptedExam, name='attempt_exams'),
    path('results/', exam_views.allresults, name='results'),
    path('history/', result_views.showExaminee_History, name='history'),
    path('rank/', result_views.showRank, name='rank'),
    path('mcqanswer/', answer_views.showMcqAnswer, name='mcqanswer'),
    path('cusquestion/',exam_views.showCustomQuestions, name='cusquestion'),
    path('question/', exam_views.showQuestions, name='question'),
    path('mcqquestion/', exam_views.showMCQQuestions, name='mcqquestion'),
    path('answer/', answer_views.showAnswer, name='answer'),
    path('cusanswer/', answer_views.showCustomAnswer, name='cusanswer'),
    # path('users/', acc_views.show_all_user, name='showuser' ),
    path('addexam/', exam_views.addExam),
    path('addmcqquestion/', exam_views.insertMcqQuestion),
    path('addanswer/', answer_views.insertAnswer),
    path('addquestion/', exam_views.AddQuestion),
    path('addcustomquestion/', exam_views.AddCustomQuestion),
    path('examshistory/', exam_views.ExamHistory),
    path('createprofile/', acc_views.create_profile),
    path('profile/', acc_views.show_profile),
    path('joinexam/', exam_views.joinExam),
    path('indivresult/<int:exam_id>', exam_views.individual_result, name='indivresult'),
    path('examresult/<int:exam_id>', exam_views.exam_result, name='examresult'),
    path('verify/<str:uid>', acc_views.verify_account),
    path('showsubmissions/<int:exam_id>',exam_views.showSubmissions),
    path('examranks/<int:exam_id>',exam_views.exam_ranks),
    path('analyse/<int:exam_id>',result_views.showGraph,),
    path('participant/<int:exam_id>', exam_views.showParticipant, )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#For Testing Purpose
# if settings.DEBUG == True:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

