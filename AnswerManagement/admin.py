from django.contrib import admin
from .models import Answer, ExamineeAnswer, ExamineeMCQAnswer

# Register your models here.

admin.site.register([Answer, ExamineeAnswer, ExamineeMCQAnswer])
