from django import forms
from App.models import Company
from django.core.exceptions import ValidationError

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'address', 'phone', 'description', 'logo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'address': forms.TextInput(attrs={'class': 'form-control input-full'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control input-full'}),
            'logo': forms.FileInput(attrs={
                'class': 'form-control input-full',
                'accept': 'image/png, image/jpeg, image/jpg'
            }),
        }

    def clean_logo(self):
        logo = self.cleaned_data.get('logo')

        if logo:
            valid_extensions = ['png', 'jpg', 'jpeg']
            extension = logo.name.split('.')[-1].lower()

            if extension not in valid_extensions:
                raise ValidationError("Solo se permiten archivos PNG, JPG o JPEG.")

            # Validar tipo MIME para mayor seguridad
            if not logo.content_type.startswith('image/'):
                raise ValidationError("El archivo debe ser una imagen válida.")

        return logo
