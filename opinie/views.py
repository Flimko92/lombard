# coding: utf-8

from django.views.generic import ListView, DetailView
from models import kontakt
from django.views.generic.edit import CreateView
from django.shortcuts import render

class KontaktCreateView(CreateView):
    model = kontakt
    fields = ['imie_i_nazwisko', 'email', 'telefon', 'miejscowosc', 'rodzaj_nieruchomosci', 'uwagi', ]