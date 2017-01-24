# coding: utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import force_bytes
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from multiselectfield import MultiSelectField


class photos (models.Model):

    name = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='photos/')

    def __unicode__(self):
        return u"%s" % (self.name)


class product_detail (models.Model):

    APPLE = 'APPLE'
    HUAWEI = 'HUAWEI'
    SAMSUNG = 'SAMSUNG'
    LG = 'LG'
    MICROSOFT = 'MICROSOFT'
    LENOVO = 'LENOVO'
    ASUS = 'ASUS'
    SONY = 'SONY'
    INNY = 'INNY'

    IOS = 'IOS'
    ANDROID = 'ANDROID'
    WINDOWS = 'WINDOWS'

    ZLOTO333 = 'ZŁOTO333'
    ZLOTO375 = 'ZŁOTO375'
    ZLOTO585 = 'ZŁOTO585'
    ZLOTO750 = 'ZŁOTO750'
    SREBRO = 'SREBRO'

    KOLCZYKI = 'KOLCZYKI'
    PIERSCIONKI = 'PIERŚCIONKI'
    NASZYJNIKI = 'NASZYJNIKI'
    BRANSOLETKI = 'BRANSOLETKI'
    WISIORKI = 'WISIORKI'
    LANCUSZKI = 'ŁAŃCUSZKI'
    BROSZKI = 'BROSZKI'

    BIZUTERIA = 'BI'
    TELEFONY = 'TELEFON'
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
        (WINDOWS, 'Windows'),
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
        (ZLOTO333, 'Złoto Próba 333'),
        (ZLOTO375, 'Złoto Próba 375'),
        (ZLOTO585, 'Złoto Próba 585'),
        (ZLOTO750, 'Złoto Próba 750'),
        (SREBRO, 'Srebro'),
    )

    PRODUCT_CHOICES = (
        (BIZUTERIA, 'Biżuteria'),
        (TELEFONY, 'Telefony'),
        (TABLETY, 'Tablety'),
        (LAPTOPY, 'Laptopy'),
        (INNE, 'Inne'),
    )

    SIZE_CHOICES = (
        ('8', '8'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('18', '18'),
    )

    name = models.CharField(max_length=120)
    type_of_product = models.CharField(choices=PRODUCT_CHOICES, max_length=12, default=INNE)
    producent = models.CharField(choices=PRODUCENT_CHOICES, max_length=12, blank=True)
    system = models.CharField(choices=SYSTEM_CHOICES, blank=True, max_length=7)
    inch = models.PositiveIntegerField(null=True, blank=True)
    memory = models.PositiveIntegerField(null=True, blank=True)
    type = models.CharField(choices=TYPE_CHOICES, blank=True, max_length=15)
    material = models.CharField(choices=MATERIAL_CHOICES, blank=True, max_length=10)
    size = MultiSelectField(choices=SIZE_CHOICES, blank=True)
    fotos = models.ImageField(upload_to='glowne/', blank=True)
    photo = models.ManyToManyField(photos, blank=True)
    desription = models.TextField()
    prize = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.PositiveIntegerField()
    pub_date = models.TimeField(auto_now_add=True, auto_now=False)
    edit_date = models.TimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return u"%s / %s" % (self.id, self.name)

    def get_absolute_url(self):
        return reverse_lazy('produkty:product_detail_list', kwargs={})









