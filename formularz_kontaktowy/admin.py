# coding: utf-8

from django.contrib import admin
from models import kontakt

class KontaktAdmin(admin.ModelAdmin):
    list_display = ('imie_i_nazwisko', 'email', 'telefon', 'wiadomosc')
    pass
admin.site.register(kontakt, KontaktAdmin)
