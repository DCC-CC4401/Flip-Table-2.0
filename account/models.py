from django.db import models
from django.contrib.auth.models import User


class Peddler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    cash = models.BooleanField(default=True)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    social = models.BooleanField(default=False)
    available = models.BooleanField(default=False)

    def __str__(self):
        return "Peddler - " + self.user.username


class Established(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    cash = models.BooleanField(default=True)
    credit = models.BooleanField(default=False)
    debit = models.BooleanField(default=False)
    social = models.BooleanField(default=False)
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return "Established - " + self.user.username


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    f_peddler = models.ManyToManyField(Peddler, blank=True)
    f_established = models.ManyToManyField(Established, blank=True)

    def __str__(self):
        return "Client - " + self.user.username
