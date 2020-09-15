from django.db import models

from Accounts.models import Examinee, Examiner


# Create your models here.

class Exam(models.Model):
    examiner_id = models.ForeignKey(Examiner, on_delete=models.SET_NULL, null=True, default=1)
    exam_code = models.IntegerField()
    exam_title = models.CharField(max_length=200)
    exam_marks = models.IntegerField()
    exam_date_time = models.DateTimeField()
    exam_duration = models.CharField(max_length=20)

    def __str__(self):
        return self.exam_title
