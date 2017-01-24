# coding: utf-8

from django.contrib import admin
from models import product_detail, photos


class Product_detailAdmin(admin.ModelAdmin):
    list_display = ('id' ,'__unicode__', 'prize')
    pass

admin.site.register(product_detail, Product_detailAdmin)

class PhotosAdmin(admin.ModelAdmin):
    list_display = ('name', 'foto')
    pass

admin.site.register(photos, PhotosAdmin)

