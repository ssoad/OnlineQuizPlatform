from django.db import models

from Accounts.models import Examinee, Examiner
from ExamManagement.models import Exam


# Create your models here.
class Result(models.Model):
    examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    marks = models.FloatField(null=False, default=0)

    def __str__(self):
        return str(self.examinee.user.username + " " + self.exam.exam_title + " " + str(self.marks))
