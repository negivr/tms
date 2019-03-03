from django.db import models
from django.utils import timezone


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(default=timezone.now)
    ssn = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Contractor(models.Model):
    name = models.CharField(max_length=100)
    fein = models.CharField(max_length=9)
    address = models.CharField(max_length=150)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



