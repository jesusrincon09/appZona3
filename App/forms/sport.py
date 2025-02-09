from django import forms
from App.models import Sport

class SportForm(forms.ModelForm):
    
    class Meta:
        model = Sport
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'description': forms.Textarea(attrs={'class': 'form-control input-full'})
        }
        