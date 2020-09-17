from django.db import models
from ExamManagement.models import MCQQuestion, CustomQuestion
from Accounts.models import Examinee


# Create your models here.

class Answer(models.Model):
    corr_ans = models.CharField(max_length=200)
    question = models.ForeignKey(MCQQuestion, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id) + ".Answer of question:" + str(self.question.question_text) + str(
            "(" + self.question.question.exam.exam_title + ")")


# class ExamineeMCQAnswer(models.Model):
#     submitted_option = models.CharField(max_length=200, blank=True, null=True)
#     mcq_question = models.ForeignKey(MCQQuestion, on_delete=models.SET_NULL, null=True, default=1)
#     examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)
#
#     def __str__(self):
#         return str(self.id) + ".Answer Script:" + str(self.examinee.user.username)


class ExamineeCustomAnswer(models.Model):
    submitted_answer = models.CharField(max_length=1000, blank=True, null=True)

    custom_question = models.ForeignKey(CustomQuestion, on_delete=models.SET_NULL, null=True, default=1)

    examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.id) + ".Answer Script:" + str(self.examinee.user.username)
