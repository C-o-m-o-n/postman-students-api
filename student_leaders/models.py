from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    area_of_interest = models.CharField(max_length=255)
    
    def __str__(self):
      return self.name

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    picture_url = models.URLField(blank=True)
    # social_links = models.JSONField()
    github_link = models.URLField(blank=True)
    x_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
      
    
    def __str__(self):
      return self.name

class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    topic = models.CharField(max_length=255)
    speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL, blank=True, null=True)
    EVENT_TYPE_CHOICES = (
        ('virtual', 'virtual'),
        ('in-person', 'in-person'),
        ('hybrid', 'hybrid'),)
    event_type = models.CharField(max_length=200, choices=EVENT_TYPE_CHOICES, default='virtual')
    
    def __str__(self):
      return self.topic
      
class Event_report(models.Model):
  event_date = models.DateField()
  event_time = models.TimeField()
  speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL, blank=True, null=True)
  registered_students = models.IntegerField()
  attendees = models.IntegerField()
  college_name = models.CharField(max_length=255)
  collaboring_college = models.CharField(max_length=255)
  EVENT_TYPE_CHOICES = (
        ('virtual', 'virtual'),
        ('in-person', 'in-person'),
        ('hybrid', 'hybrid'), )
  event_type = models.CharField(max_length=200, choices=EVENT_TYPE_CHOICES, default='virtual')
  platform = models.CharField(max_length=255)
  media_link = models.URLField(blank=True)
    
  def __str__(self):
    return self.topic

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self):
      return self.student



