from datetime import datetime
from django import forms
from App.models import Reservation

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['client_name', 'client_cell', 'client_email', 'space', 'reservation_start', 'reservation_end']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'client_cell': forms.NumberInput(attrs={
                'class': 'form-control input-full',
                'min': '0',
                'oninput': "this.value = Math.max(this.value, 0)"
            }),
            'client_email': forms.EmailInput(attrs={'class': 'form-control input-full'}),
            'space': forms.Select(attrs={'class': 'form-control input-full'}),
            'reservation_start': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker'}),
            'reservation_end': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker'}),
        }