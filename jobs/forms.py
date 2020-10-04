from django import forms

from .models import *


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job

        fields = ['title', 'company', 'location', 'job_type', 'category', 'description']
        widgets = {
            'job_type': forms.RadioSelect
        }


class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = []
