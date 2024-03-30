from django.urls import path, include
from rest_framework import routers
from student_leaders import views  

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Postman Students Leaders (LeaderHub) API",
      default_version='v-0.0.1',
      description="""
      The Postman Student Leader Program API empowers Student Leaders to efficiently manage events and speaker data. It provides a comprehensive interface for CRUD operations (Create, Read, Update, Delete) on events and speakers. Authorized users can create informative event listings, associate speakers with their expertise, and even manage speaker social media profiles. This API streamlines event organization and facilitates the creation of engaging experiences for student leaders.
      """,
      terms_of_service="http://127.0.0.1/terms/",
      contact=openapi.Contact(email="comon928@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'reports', views.EventReportViewSet)
router.register(r'registrations', views.RegistrationViewSet)
router.register(r'speakers', views.SpeakerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('terms/', views.terms, name='terms'),
]