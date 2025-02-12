from django import forms
from App.models import Sport

class SportForm(forms.ModelForm):
    description = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Descripcion',  'rows': '7','maxlength': '1000'}),
    )
    
    class Meta:
        model = Sport
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'description': forms.Textarea(attrs={'class': 'form-control input-full'})
        }
        error_messages = {
            'name': {
                'required': "El nombre del deporte es obligatorio.",
            },
            'description': {
                'required': "La descripción del deporte es obligatoria.",
            }
        }