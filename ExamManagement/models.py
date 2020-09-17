from django.db import models

from Accounts.models import Examinee, Examiner


# Create your models here.

class Exam(models.Model):
    examiner = models.ForeignKey(Examiner, on_delete=models.SET_NULL, null=True, default=1)
    exam_code = models.IntegerField(unique=True)
    exam_title = models.CharField(max_length=200)
    exam_marks = models.IntegerField(null=False, default=100)
    exam_date_time = models.DateTimeField()
    exam_duration = models.IntegerField(null=False, default=60)

    def __str__(self):
        return self.exam_title


class AttemptedExam(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE)

    def __str__(self):
        return str("Exam:-"+self.exam.exam_title + ",Examinee:-" + self.examinee.user.username)


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
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+"."+str(self.question_text + "(" + self.question.exam.exam_title + ")")


class CustomQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + "." + str(self.question_text + "(" + self.question.exam.exam_title + ")")
