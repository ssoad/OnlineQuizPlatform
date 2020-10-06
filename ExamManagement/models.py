from django.db import models
import datetime
from Accounts.models import Examinee, Examiner


# Create your models here.
# from AnswerManagement.models import ExamineeCustomAnswer


class Exam(models.Model):
    examiner = models.ForeignKey(Examiner, on_delete=models.SET_NULL, null=True, default=1)
    exam_code = models.IntegerField(unique=True)
    exam_title = models.CharField(max_length=200)
    exam_marks = models.IntegerField(null=False, default=100)
    exam_date_time = models.DateTimeField()
    exam_duration = models.IntegerField(null=False, default=60)
    exam_question = models.FileField(upload_to='exam/questions', null=False, blank=False,
                                     default='exam/questions/sample.pdf')

    def getParticipant(self):
        participant = len(AttemptedExam.objects.filter(exam_id=self.id))
        return participant

    def getSubmission(self):
        from AnswerManagement.models import ExamineeAnswer
        submissions = len(ExamineeAnswer.objects.filter(exam_id=self.id))
        return submissions

    def isRunning(self):
        timezone = self.exam_date_time.tzinfo
        mins = self.exam_duration
        mins_added = datetime.timedelta(minutes=mins)
        datetime_start = self.exam_date_time
        future_date_and_time = datetime_start + mins_added
        now = datetime.datetime.now(timezone) + datetime.timedelta(hours=6)
        if now < future_date_and_time:
            # print("Running")
            return True
        return False

    def __str__(self):
        return self.exam_title


class AttemptedExam(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
    examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE)
    submit = models.BooleanField(default=False, null=False, blank=False)

    def hasReturnAttachment(self):
        from ResultManagement.models import Result
        attachment = Result.objects.filter(examinee=self.examinee, exam=self.exam)
        # print("Function:", attachment[0])
        if attachment:
            attachment = attachment[0].attachment
            if attachment:
                return True,
            else:
                return False

    @property
    def ReturnAttachment(self):
        from ResultManagement.models import Result
        attachment = Result.objects.filter(examinee=self.examinee, exam=self.exam)
        attachment_url = attachment[0].attachment.url
        if self.hasReturnAttachment():
            #print("URL", attachment)
            return attachment_url

    def __str__(self):
        return str("Exam: " + self.exam.exam_title + ",Examinee: " + self.examinee.user.username)


class Question(models.Model):
    marks = models.IntegerField(null=False, default=100)
    time_limit = models.IntegerField(null=False, default=60)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.exam.exam_title


class MCQQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    ques_marks = models.IntegerField(blank=False, null=False, default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + "." + str(self.question_text + "(" + self.question.exam.exam_title + ")")


class CustomQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    ques_marks = models.IntegerField(blank=False, null=False, default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + "." + str(self.question_text + "(" + self.question.exam.exam_title + ")")
