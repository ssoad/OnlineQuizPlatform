from django.contrib import admin

from .models import Exam, AttemptedExam

# Register your models here.
admin.site.register([Exam, AttemptedExam])
