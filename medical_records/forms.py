from django import forms
from .models import PersonalDetails, MedicalHistory


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = PersonalDetails
        fields = ['name', 'age', 'gender', 'contact']


class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = '__all__'
