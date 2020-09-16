from django.contrib import admin
from .models import Answer, ExamineeMCQAnswer, ExamineeCustomAnswer

# Register your models here.

admin.site.register([Answer, ExamineeMCQAnswer, ExamineeCustomAnswer])
