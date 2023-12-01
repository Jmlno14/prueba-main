# ------------------------------------------------------------------
# DJANGO
# ------------------------------------------------------------------

from django import forms

# ------------------------------------------------------------------
# MODELO
# ------------------------------------------------------------------

from .models import Country

# ------------------------------------------------------------------
# FORMULARIO
# ------------------------------------------------------------------
class NuevoCountryForm(forms.ModelForm):
    """Form definition for Country."""
    class Meta:
        """Meta definition for Countryform."""
        # Modelo al que se aplica el formulario
        model = Country
        # Campos usados en el formulario
        fields = (
                'nombreCountry',
                'population',
                'nombreCountry',
                'id_country',
                'continent_Country',
                'region_Country',
                'surface_Country',
                'indep_year_country',
                'population',
                'life_expectancy',
                'GNP',
                'GNPold',
                'local_name',
                'goverment',
                'state_head',
                'capital_country',
                'code2',
                'siglaCountry',
                'activoCountry'
        )
        # Labels de los campos del formulario
        labels = {
                'nombreCountry':'nombreCountry',
                'population': 'population',
                'nombreCountry':'nombreCountry',
                'id_country':'id_country',
                'continent_Country':'continent_Country',
                'region_Country':'region_Country',
                'surface_Country':'surface_Country',
                'indep_year_country':'indep_year_country',
                'population':'population',
                'life_expectancy':'life_expectancy',
                'GNP':'GNP',
                'GNPold':'GNPold',
                'local_name':'local_name',
                'goverment':'goverment',
                'state_head':'state_head',
                'capital_country':'capital_country',
                'code2':'code2',
                'siglaCountry':'siglaCountry',
                'activoCountry': 'activoCountry'
        }
                # Espacio para agregar características a los campos
        widgets = {
            'activoCountry': forms.CheckboxInput(
                attrs={'class': 'ContainerCountryFormSelect'}
            ),
            'nombreCountry': forms.TextInput(
                attrs={
                    'class': 'ContainerCountryFormName',
                    'placeholder': 'Nombre Country'
                }
            ),
            'siglaCountry': forms.TextInput(
                attrs={
                    'class': 'ContainerCountryFormName',
                    'placeholder': 'Sigla Country'
                }
            ),
        }