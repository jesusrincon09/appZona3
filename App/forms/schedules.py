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
    def clean(self):
        cleaned_data = super().clean()
        day = cleaned_data.get('day')
        startime = cleaned_data.get('startime')
        endtime = cleaned_data.get('endtime')

        if startime and endtime and startime >= endtime:
            self.add_error('startime', "La hora de inicio debe ser menor que la hora de fin.")
            self.add_error('endtime', "La hora de fin debe ser mayor que la hora de inicio.")

        overlapping_schedules = Schedule.objects.filter(day=day).exclude(id=self.instance.id)

        for schedule in overlapping_schedules:
            existing_start = schedule.startime.strftime('%I:%M %p')
            existing_end = schedule.endtime.strftime('%I:%M %p')
            new_start = startime.strftime('%I:%M %p')
            new_end = endtime.strftime('%I:%M %p')

            if (schedule.startime <= startime < schedule.endtime) or (schedule.startime < endtime <= schedule.endtime) or (startime <= schedule.startime and endtime >= schedule.endtime):
                self.add_error('startime', f"Este horario ({new_start} - {new_end}) se cruza con otro ({existing_start} - {existing_end}).")

        return cleaned_data