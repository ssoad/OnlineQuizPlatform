from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Examinee(models.Model):
    organization = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.first_name + " " + self.user.last_name)


class Examiner(models.Model):
    organization = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.first_name + " " + self.user.last_name)
