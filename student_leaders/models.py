from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    area_of_interest = models.CharField(max_length=255)

class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    topic = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255, blank=True)

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

