from django.contrib import admin
from .models import Examinee, Examiner, Profile

# Register your models here.
admin.site.register([Examinee, Examiner, Profile])
