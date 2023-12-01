from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.

# ------------------------------------------------------------------
# APIS
# ------------------------------------------------------------------
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    # DetailView
    RetrieveAPIView,
    # Delete
    DestroyAPIView,
    # Actualizar
    UpdateAPIView,
    # Recupera y actualiza
    RetrieveUpdateAPIView,
    # Recupera y elimina
    RetrieveDestroyAPIView,
)

from .serializer import (
    CountrysSerializer
)
# ------------------------------------------------------------------
# VISTAS A USAR
# ------------------------------------------------------------------

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# ------------------------------------------------------------------
# MODELOS
# ------------------------------------------------------------------
from .models import Country

# ------------------------------------------------------------------
# FORMULARIOS
# ------------------------------------------------------------------

from .forms import NuevoCountryForm

# ------------------------------------------------------------------
# CREAR Country
# ------------------------------------------------------------------

class NuevoCountry(CreateView):
    # Modelo usado para la vista
    model = Country
    # Template usado en la vista
    template_name = 'Country/NuevoCountry.html'
    # Contexto usado para la impresión en el html
    context_object_name = 'NuevoCountry'
    # formulario usado en la vista
    form_class = NuevoCountryForm
    # Dirección a la que va cuando se ejecuta el submit
    success_url = reverse_lazy('inicio_app:home')

    def form_valid(self, form):
        # Guardando los datos del formulario
        Country = form.save(commit=False)
        Country.save()
        # Return del formulario completado
        return super(NuevoCountry, self).form_valid(form)


# ------------------------------------------------------------------
# API CREAR UN TRABAJO
# ------------------------------------------------------------------
class CountryAPISerializer(CreateAPIView):
    serializer_class = CountrysSerializer