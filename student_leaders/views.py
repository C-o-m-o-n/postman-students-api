from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Event, Registration, Speaker,Event_report
from .serializers import StudentSerializer, EventSerializer, RegistrationSerializer, SpeakerSerializer, EventReportSerializer

from django.http import HttpResponse

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


def terms(request):
    # <h1>Terms of Service</h1>
    terms_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Postman Student Leader Program API - Terms of Service</title>
  <style>
    body {
      font-family: sans-serif;
      margin: 2rem;
    }
    h1, h2 {
      margin-bottom: 1rem;
    }
  </style>
</head>
<body>
  <h1>Terms of Service for Postman Student Leader Program API</h1>

  <p>These Terms of Service ("Terms") govern your access to and use of the Postman Student Leader Program API ("API"). By accessing or using the API, you agree to be bound by these Terms. If you disagree with any part of these Terms, you may not access or use the API.</p>

  <h2>Definitions</h2>

  <ul>
    <li><strong>API:</strong> The Postman Student Leader Program API, a web service that allows authorized users to manage events and speakers associated with the program.</li>
    <li><strong>Authorized User:</strong> An individual or entity granted permission to access and use the API.</li>
    <li><strong>Content:</strong> Any data, information, or materials uploaded, submitted, or stored through the API.</li>
    <li><strong>You:</strong> The individual or entity accessing or using the API.</li>
  </ul>

  <h2>Use of the API</h2>

  <p><strong>3.1 You may only use the API for lawful purposes and in accordance with these Terms.</strong></p>
  <p><strong>3.2 You are responsible for all activity that occurs under your account.</strong></p>
  <p><strong>3.3 You will not:</strong></p>
  <ul>
    <li>Disrupt or interfere with the API or its servers.</li>
    <li>Attempt to gain unauthorized access to the API or any other system or network.</li>
    <li>Use the API to transmit any unlawful, harmful, threatening, abusive, harassing, defamatory, obscene, hateful, or racially or ethnically offensive material.</li>
    <li>Use the API to violate the intellectual property rights of any third party.</li>
    <li>Use the API to violate any applicable laws or regulations.</li>
  </ul>

  <h2>Content</h2>

  <p><strong>4.1 You are solely responsible for any Content you upload, submit, or store through the API.</strong></p>
  <p><strong>4.2 You retain all ownership rights to your Content. However, by submitting Content through the API, you grant us a non-exclusive, worldwide, royalty-free license to use, reproduce, modify, publish, distribute, and translate your Content for the purpose of operating and providing the API.</strong></p>
  <p><strong>4.3 You represent and warrant that your Content does not violate the intellectual property rights or any other rights of any third party.</strong></p>

  <h2>Disclaimer</h2>

  <p>THE API IS PROVIDED "AS IS" AND WITHOUT WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED. WE DISCLAIM ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. WE DO NOT WARRANT THAT THE API WILL BE UNINTERRUPTED, SECURE, OR ERROR-FREE.</p>

  <h2>Limitation of Liability</h2>

  <p>IN NO EVENT SHALL WE BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES ARISING OUT OF OR IN CONNECTION WITH YOUR USE OF THE API, EVEN IF WE HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.</p>

  <h2>Termination</h2>
  <h2>Governing Law and Jurisdiction</h2>
  <h2>Entire Agreement</h2>
  <h2>Amendments</h2>
  <h2>Severability</h2>
  <h2>Waiver</h2>
  <h2>Contact Us</h2>

</body>
</html>

    """
    return HttpResponse(terms_content)
    
    
    
    
    