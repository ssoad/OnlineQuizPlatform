from django.contrib import admin

from .models import Result, Rank, ExamineeHistory

# Register your models here.
admin.site.register([Result, Rank, ExamineeHistory])
