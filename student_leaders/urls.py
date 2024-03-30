from django.urls import path, include
from rest_framework import routers
from student_leaders import views  # or views if using custom views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'reports', views.EventReportViewSet)
router.register(r'registrations', views.RegistrationViewSet)
router.register(r'speakers', views.SpeakerViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

