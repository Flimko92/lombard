# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse_lazy

class kontakt(models.Model):


    imie_i_nazwisko = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.PositiveIntegerField()
    wiadomosc = models.TextField(max_length=500)

    class Meta:
        ordering = ['imie_i_nazwisko']

    def __unicode__(self):
        return u"Imie i nazwisko: %s" % (self.imie_i_nazwisko)

    def get_absolute_url(self):
        return reverse_lazy('kontakt:wyslij_kontakt', kwargs={})
