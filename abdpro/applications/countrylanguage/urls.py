from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "countrylanguage_app"

urlpatterns = [
        path('Nuevocountrylanguage/',
                views.Nuevocountrylanguage.as_view(),
                name='Nuevocountrylanguage'),

]