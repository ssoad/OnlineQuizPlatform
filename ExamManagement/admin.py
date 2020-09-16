from django.contrib import admin

from .models import Exam, AttemptedExam, Questions

# Register your models here.
admin.site.register([Exam, AttemptedExam,Questions])
