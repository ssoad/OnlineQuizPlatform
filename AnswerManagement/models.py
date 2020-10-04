from django.db import models
from ExamManagement.models import MCQQuestion, CustomQuestion, Exam, AttemptedExam
from Accounts.models import Examinee
from django.utils import timezone
import datetime
import pytz


# Create your models here.

class Answer(models.Model):
    corr_ans = models.CharField(max_length=200)
    question = models.ForeignKey(MCQQuestion, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id) + ".Answer of question:" + str(self.question.question_text) + str(
            "(" + self.question.question.exam.exam_title + ")")


class ExamineeMCQAnswer(models.Model):
    submitted_option = models.CharField(max_length=200, blank=True, null=True)
    mcq_question = models.ForeignKey(MCQQuestion, on_delete=models.SET_NULL, null=True, default=1)
    examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id) + ".Answer Script:" + str(self.examinee.user.username)


class ExamineeAnswer(models.Model):
    # submitted_answer = models.CharField(max_length=1000, blank=True, null=True)
    answer = models.FileField(null=False, blank=False, upload_to='exam/answers/', default='exam/answers/sample.pdf')
    # custom_question = models.ForeignKey(CustomQuestion, on_delete=models.SET_NULL, null=True, default=1)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, default=1, null=True, blank=True)
    examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    graded = models.BooleanField(default=False)
    done_late = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ".Answer Script:" + str(self.examinee.user.username)

    def checkLate(self):
        timezone = self.exam.exam_date_time.tzinfo
        mins = self.exam.exam_duration
        mins_added = datetime.timedelta(minutes=mins)
        datetime_start = self.exam.exam_date_time
        future_date_and_time = datetime_start + mins_added
        now = datetime.datetime.now(timezone) + datetime.timedelta(hours=6)
        #print('Now:', now)
        #print('Due Time:', future_date_and_time)
        if now > future_date_and_time:
            self.done_late = True
            #print("Late Submission")
        else:
            self.done_late = False
            #print("Not Late Submission")
