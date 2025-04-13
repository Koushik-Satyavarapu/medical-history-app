from django.contrib import admin
from .models import PersonalDetails, MedicalHistory

admin.site.register(PersonalDetails)
admin.site.register(MedicalHistory)