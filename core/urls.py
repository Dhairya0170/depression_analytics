from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # <-- 1. Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('depression_analytics.urls')),
    
    # 2. Add this new path for the front door!
    # The empty quotes '' mean this is the default homepage.
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]