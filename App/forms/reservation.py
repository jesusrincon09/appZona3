from datetime import datetime
from zoneinfo import ZoneInfo
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
    
    def clean(self):
        cleaned_data = super().clean()
        reservation_start = cleaned_data.get('reservation_start')
        reservation_end = cleaned_data.get('reservation_end')
        space = cleaned_data.get('space')
        overlapping_reservations = Reservation.objects.filter(space=space).exclude(id=self.instance.id)
        
        for reservation in overlapping_reservations:
            if (reservation_start <= reservation.reservation_start < reservation_end) or (reservation_start < reservation.reservation_end <= reservation_end) or (reservation_start <= reservation.reservation_start and reservation_end >= reservation.reservation_end):
                self.add_error('reservation_start', f"Esta reserva se cruza con otra.")
                self.add_error('reservation_end', f"Esta reserva se cruza con otra.")
        
        if reservation_start and reservation_end and reservation_start >= reservation_end:
            self.add_error('reservation_start', "La fecha de inicio debe ser menor que la fecha de fin.")
            self.add_error('reservation_end', "La fecha de fin debe ser mayor que la fecha de inicio.")

        timezone = ZoneInfo('America/Bogota')
        date_now = datetime.now(timezone)
        if reservation_start and reservation_start < date_now:
            self.add_error('reservation_start', "La fecha de inicio debe ser mayor que la fecha actual.")

        return cleaned_data