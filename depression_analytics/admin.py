from django.contrib import admin
from .models import Assessment

# This registers your model so it shows up in the admin panel
admin.site.register(Assessment)