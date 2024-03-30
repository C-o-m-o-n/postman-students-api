from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Event, Registration, Speaker,Event_report
from .serializers import StudentSerializer, EventSerializer, RegistrationSerializer, SpeakerSerializer, EventReportSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class EventReportViewSet(viewsets.ModelViewSet):
    queryset = Event_report.objects.all()
    serializer_class = EventReportSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


