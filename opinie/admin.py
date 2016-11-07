# coding: utf-8

from django.contrib import admin
from models import opinia

class OpinieAdmin(admin.ModelAdmin):
    list_display = ('imie', 'ocena', 'tresc', 'data')
    pass
admin.site.register(opinia, OpinieAdmin)
