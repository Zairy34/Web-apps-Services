# myapp/forms.py

from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['name', 'phone_number', 'service', 'service_date', 'request']

    service_choices = [
        ('Tech', 'Tech'),
        ('Plumbing', 'Plumbing'),
        ('Carpenters', 'Carpenters'),
        ('Computer Fixing', 'Computer Fixing'),
        ('Mounting', 'Mounting'),
        ('fitness Trainer','fitness Trainer'),
        ('Software Fixing','Software Fixing'),
        ('Software building','Software Building'),
        ('Electrcian','Electrcian'),
        ('Install Equipments''Install Equipments'),
        ('Fix Equipments','Fix Equipments')
    ]
    service = forms.ChoiceField(choices=service_choices)
