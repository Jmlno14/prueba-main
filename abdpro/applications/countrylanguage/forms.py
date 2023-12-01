# ------------------------------------------------------------------
# DJANGO
# ------------------------------------------------------------------

from django import forms

# ------------------------------------------------------------------
# MODELO
# ------------------------------------------------------------------

from .models import countrylanguage

# ------------------------------------------------------------------
# FORMULARIO
# ------------------------------------------------------------------
class NuevocountrylanguageForm(forms.ModelForm):
    """Form definition for countrylanguage."""
    class Meta:
        """Meta definition for countrylanguageform."""
        # Modelo al que se aplica el formulario
        model = countrylanguage
        # Campos usados en el formulario
        fields = (
                'nombrecountrylanguage',
                'id_country',
                'countrylanguage',
                'isOfficial',
                'percentage',
                'siglacountrylanguage',
                'activocountrylanguage',
            
        )
        # Labels de los campos del formulario
        labels = {
                'nombrecountrylanguage':'nombreCountrylanguage',
                'id_country':'id_country',
                'countrylanguage':'countrylanguage',
                'isOfficial':'isOfficial',
                'percentage':'percentage',
                'siglacountrylanguage':'siglacountrylanguage',
                'activocountrylanguage':'activocountrylanguage',
                
        }
                # Espacio para agregar características a los campos
        widgets = {
            'activocountrylanguage': forms.CheckboxInput(
                attrs={'class': 'ContainercountrylanguageFormSelect'}
            ),
            'nombrecountrylanguage': forms.TextInput(
                attrs={
                    'class': 'ContainercountrylanguageFormName',
                    'placeholder': 'Nombre countrylanguage'
                }
            ),
            'siglacountrylanguage': forms.TextInput(
                attrs={
                    'class': 'ContainercountrylanguageFormName',
                    'placeholder': 'Sigla countrylanguage'
                }
            ),
        }