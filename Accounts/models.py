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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pro_pic = models.ImageField(upload_to='images/profile', default='images/profile/Default.jpg', null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True)

    def __str__(self):
        return str(self.user.first_name + " " + self.user.last_name)


class Verification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return str(self.user.username)
