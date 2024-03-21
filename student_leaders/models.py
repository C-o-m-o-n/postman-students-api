from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    area_of_interest = models.CharField(max_length=255)

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    picture_url = models.URLField(blank=True)
    social_links = models.JSONField(default=list)

class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    topic = models.CharField(max_length=255)
    speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL, blank=True, null=True)

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)



