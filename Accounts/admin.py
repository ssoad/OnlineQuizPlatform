from django.contrib import admin
from .models import Examinee,Examiner

# Register your models here.
admin.site.register([Examinee, Examiner])
