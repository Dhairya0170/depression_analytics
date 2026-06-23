from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssessmentViewSet

# 1. Create a router (this acts as an automatic address book)
router = DefaultRouter()

# 2. Register our ViewSet with the router
# The 'assessments' part means the URL will be: /assessments/
router.register(r'assessments', AssessmentViewSet)

# 3. Expose these URLs
urlpatterns = [
    path('', include(router.urls)),
]