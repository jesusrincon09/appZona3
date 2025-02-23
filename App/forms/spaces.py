from django import forms
from App.models import Spaces, Schedule

class SpacesForm(forms.ModelForm):

    class Meta:
        model = Spaces
        fields = ['name', 'sport', 'description', 'schedule', 'numberplayers']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'sport': forms.Select(attrs={'class': 'form-control input-full'}),
            'description': forms.Textarea(attrs={'class': 'form-control input-full'}),
            'numberplayers': forms.NumberInput(attrs={
                'class': 'form-control input-full',
                'min': '1',
                'oninput': "this.value = Math.max(this.value, 1)"
            })
        }

    schedule = forms.ModelMultipleChoiceField(
        queryset=Schedule.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control input-full style-select2'})
    )

