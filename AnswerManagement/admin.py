from django.contrib import admin
from .models import Answer, ExamineeCustomAnswer

# Register your models here.

admin.site.register([Answer, ExamineeCustomAnswer])
