from django.contrib import admin

from .models import Exam, AttemptedExam, Question, MCQQuestion, CustomQuestion

# Register your models here.
admin.site.register([Exam, AttemptedExam, Question, MCQQuestion, CustomQuestion])
