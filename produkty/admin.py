# coding: utf-8

from django.contrib import admin
from models import product_detail


class Product_detailAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'prize')
    pass

admin.site.register(product_detail, Product_detailAdmin)



