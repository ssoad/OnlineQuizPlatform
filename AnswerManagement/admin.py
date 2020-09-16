from django.contrib import admin
from .models import Answer, ExamineeAnswer

# Register your models here.

admin.site.register([Answer, ExamineeAnswer])
