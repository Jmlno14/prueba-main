from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "country_app"

urlpatterns = [
        path('NuevoCountry/',
                views.NuevoCountry.as_view(),
                name='NuevoCountry'),

]