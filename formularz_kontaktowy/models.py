# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse_lazy

class kontakt(models.Model):

    MIESZKANIE = 'M'
    DOM = 'D'
    DZIALKA = 'P'
    INNE = 'I'

    RODZAJ=(
        (MIESZKANIE, ('Mieszkanie')),
        (DOM, 'Dom'),
        (DZIALKA, 'Działka'),
        (INNE, 'Inne'),
    )

    imie_i_nazwisko = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.PositiveIntegerField()
    miejscowosc = models.CharField(max_length=150)
    rodzaj_nieruchomosci = models.CharField(choices=RODZAJ, max_length=1, blank=True)
    uwagi = models.TextField(max_length=500)

    class Meta:
        ordering = ['imie_i_nazwisko']

    def __unicode__(self):
        return u"Imie i nazwisko: %s" % (self.imie_i_nazwisko)

    def get_absolute_url(self):
        return reverse_lazy('kontakt:wyslij_kontakt', kwargs={})
