from django.db import models
from ExamManagement.models import Questions

# Create your models here.

class Answer(models.Model):
    corr_ans = models.CharField(max_length=200)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+".Answer of question"+str(self.question.id)+str("("+self.question.exam.exam_title+")")

