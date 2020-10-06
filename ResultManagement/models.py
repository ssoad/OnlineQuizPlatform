from django.db import models

from Accounts.models import Examinee, Examiner
from ExamManagement.models import Exam


# Create your models here.
class Result(models.Model):
    examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    marks = models.FloatField(null=True, default=0)
    attachment = models.FileField(null=True, blank=True, upload_to='exam/returns')

    # @property
    # def attachment_url(self):
    #     if self.attachment and hasattr(self.attachment, 'url'):
    #         return self.attachment.url

    def __str__(self):
        return str(self.examinee.user.username + " " + self.exam.exam_title + " " + str(self.marks))


class Rank(models.Model):
    examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    marks = models.FloatField(null=False, default=0)
    time = models.IntegerField(null=False, default=1)

    def __str__(self):
        return str(self.examinee.user.username + " " + self.exam.exam_title + " " + str(self.marks))


class ExamineeHistory(models.Model):
    examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    date = models.DateField(null=False)
    marks = models.FloatField(null=False, default=0)
    right = models.IntegerField(null=False)
    wrong = models.IntegerField(null=False)

    # question = models.ForeignKey()

    def __str__(self):
        return str(self.examinee.user.username + " " + self.exam.exam_title + " " + str(self.marks))
