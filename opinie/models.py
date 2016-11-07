# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse_lazy

class opinia(models.Model):

    SUPER = 'S'
    DOBRZE = 'D'
    ZLE = 'Z'
    TRAGEDIA = 'T'

    RODZAJ=(
        (SUPER, ('Super')),
        (DOBRZE, 'Dobrze'),
        (ZLE, 'Źle'),
        (TRAGEDIA, 'Tragedia'),
    )

    imie = models.CharField(max_length=100)
    ocena = models.CharField(choices=RODZAJ, max_length=1, blank=True)
    tresc = models.TextField(max_length=500)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data']

    def __unicode__(self):
        return u"Imie: %s" % (self.imie)

    def get_absolute_url(self):
       return reverse_lazy('opinie:lista_opini', kwargs={})
