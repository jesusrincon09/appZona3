from django import forms
from App.models import Schedule

class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['day', 'startime', 'endtime']

        widgets = {
            'day': forms.Select(attrs={'class': 'form-select'}),
            'startime': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'endtime': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
