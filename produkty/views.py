# coding: utf-8

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from models import product_detail
from django.db.models import Q


class Product_detailListView (ListView):
    model = product_detail

class Product_detailCreateView (CreateView):
    model = product_detail
    fields = ['nr_kat','name', 'type_of_product', 'producent', 'system', 'size', 'memory', 'type', 'material',
              'photo', 'desription', 'prize', 'count',
              ]
class Product_detailUpdateView(UpdateView):
    model = product_detail
    fields = ['nr_kat','name', 'type_of_product', 'producent', 'system', 'size', 'memory', 'type', 'material',
              'photo', 'desription', 'prize', 'count',
    ]
    template_name = 'produkty/product_detail_update_form.html'

class Product_detailDeleteView(DeleteView):
    model = product_detail
    success_url = '/produkty/product_detail_list'

class BizuteriaListView (ListView):
    queryset = product_detail.objects.filter(type_of_product='BI')
    template_name = 'produkty/bizuteria_list.html'

class TelefonyListView (ListView):
    queryset = product_detail.objects.filter(type_of_product='TE')
    template_name = 'produkty/telefony_list.html'

class TabletyListView (ListView):
    queryset = product_detail.objects.filter(type_of_product='TA')
    template_name = 'produkty/tablety_list.html'

class LaptopyListView (ListView):
    queryset = product_detail.objects.filter(type_of_product='LA')
    template_name = 'produkty/laptopy_list.html'

class InneListView (ListView):
    queryset = product_detail.objects.filter(type_of_product='IN')
    template_name = 'produkty/inne_list.html'

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