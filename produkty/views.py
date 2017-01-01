# coding: utf-8

from django.views.generic import ListView, DetailView
from models import product_detail


class Product_detailListView (ListView):
    model = product_detail

class BizuteriaListView (ListView):
    queryset = product_detail.objects.filter(type_of_product='BI')
    template_name = 'produkty/bizuteria_list.html'

class TelefonyListView (ListView):
    model = product_detail

class TabletyListView (ListView):
    model = product_detail

class LaptopyListView (ListView):
    model = product_detail

class InneListView (ListView):
    model = product_detail

class Product_detailDetailView (DetailView):
    model = product_detail



#Przykład

# class ShotAddView (FormView):
#     form_class = ShotForm
#     template_name = 'produkty/shot_add.html'
#     success_url = 'scene_detail'
#
#     def form_valid(self, form):
#         form.save()
#         return super(ShotAddView, self).form_valid(form)