# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import force_bytes
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy


class product_detail (models.Model):

    APPLE = 'A'
    HUAWEI = 'H'
    SAMSUNG = 'S'
    LG = 'LG'
    MICROSOFT = 'M'
    LENOVO = 'LV'
    ASUS = 'AS'
    SONY = 'SN'
    INNY = 'IN'

    IOS = 'I'
    ANDROID = 'AD'

    KOLCZYKI = 'K'
    PIERSCIONKI = 'P'
    NASZYJNIKI = 'N'
    BRANSOLETKI = 'B'
    WISIORKI = 'W'
    LANCUSZKI = 'L'
    BROSZKI = 'BR'

    ZLOTO = 'Z'
    SREBRO = 'SR'

    BIZUTERIA = 'BI'
    TELEFONY = 'TE'
    TABLETY = 'TA'
    LAPTOPY = 'LA'
    INNE = 'IE'

    PRODUCENT_CHOICES = (
        (APPLE, 'Apple'),
        (HUAWEI, 'Huawei'),
        (SAMSUNG, 'Samsung'),
        (LG, 'LG'),
        (MICROSOFT, 'Microsoft'),
        (LENOVO, 'Lenovo'),
        (ASUS, 'Asus'),
        (SONY, 'Sony'),
        (INNY, 'Inny'),
    )

    SYSTEM_CHOICES = (
        (IOS, 'iOS'),
        (ANDROID, 'Android'),
    )

    TYPE_CHOICES = (
        (KOLCZYKI, 'Kolczyki'),
        (PIERSCIONKI, 'Pierścionki'),
        (NASZYJNIKI, 'Naszyjniki'),
        (BRANSOLETKI, 'Bransoletki'),
        (WISIORKI, 'Wisiorki'),
        (LANCUSZKI, 'Łańcuszki'),
        (BROSZKI, 'Broszki'),
    )

    MATERIAL_CHOICES = (
        (ZLOTO, 'Złoto'),
        (SREBRO, 'Srebro'),
    )

    PRODUCT_CHOICES = (
        (BIZUTERIA, 'Biżuteria'),
        (TELEFONY, 'Telefony'),
        (TABLETY, 'Tablety'),
        (LAPTOPY, 'Laptopy'),
        (INNE, 'Inne'),
    )

    nr_kat = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=120)
    type_of_product = models.CharField(choices=PRODUCT_CHOICES, max_length=2, default=INNE)
    producent = models.CharField(choices=PRODUCENT_CHOICES, max_length=2, blank=True)
    system = models.CharField(choices=SYSTEM_CHOICES, blank=True, max_length=2)
    size = models.PositiveIntegerField(null=True, blank=True)
    memory = models.PositiveIntegerField(null=True, blank=True)
    type = models.CharField(choices=TYPE_CHOICES, blank=True, max_length=2)
    material = models.CharField(choices=MATERIAL_CHOICES, blank=True, max_length=2)
    photo = models.ImageField(upload_to='photos/', blank=True)
    desription = models.TextField()
    prize = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.PositiveIntegerField()
    pub_date = models.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['nr_kat']

    def __unicode__(self):
        return u"%s / %s" % (self.nr_kat, self.name)

    def get_absolute_url(self):
        return reverse_lazy('produkty:product_list', kwargs={})






