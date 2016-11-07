# coding: utf-8

from django.views.generic import ListView, DetailView
from models import opinia
from django.views.generic.edit import CreateView
from django.shortcuts import render

class OpiniaListView(ListView):
    model = opinia

class OpiniaCreateView(CreateView):
    model = opinia
    fields = ['imie', 'ocena', 'tresc', ]

