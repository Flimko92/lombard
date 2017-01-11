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

class PierscionkiListView (ListView):
    queryset = product_detail.objects.filter(type='P')
    template_name = 'produkty/pierscionki_list.html'

class KolczykiListView (ListView):
    queryset = product_detail.objects.filter(type='K')
    template_name = 'produkty/kolczyki_list.html'

class NaszyjnikiListView (ListView):
    queryset = product_detail.objects.filter(type='N')
    template_name = 'produkty/naszyjniki_list.html'

class BransoletkiListView (ListView):
    queryset = product_detail.objects.filter(type='B')
    template_name = 'produkty/bransoletki_list.html'

class WisiorkiListView (ListView):
    queryset = product_detail.objects.filter(type='W')
    template_name = 'produkty/wisiorki_list.html'

class LancuszkiListView (ListView):
    queryset = product_detail.objects.filter(type='L')
    template_name = 'produkty/lancuszki_list.html'

class BroszkiListView (ListView):
    queryset = product_detail.objects.filter(type='BR')
    template_name = 'produkty/broszki_list.html'

class ZlotoListView (ListView):
    queryset = product_detail.objects.filter(material='Z')
    template_name = 'produkty/zloto_list.html'

class SrebroListView (ListView):
    queryset = product_detail.objects.filter(type='SR')
    template_name = 'produkty/srebro_list.html'

class TelefonyListView (ListView):
    queryset = product_detail.objects.filter(type_of_product='TE')
    template_name = 'produkty/telefony_list.html'

class IosListView (ListView):
    queryset = product_detail.objects.filter(system='I')
    template_name = 'produkty/ios_list.html'

class AndroidListView (ListView):
    queryset = product_detail.objects.filter(system='AD')
    template_name = 'produkty/produkty_list.html'

class WindowsListView (ListView):
    queryset = product_detail.objects.filter(system='WI')
    template_name = 'produkty/windows_list.html'

class TabletyListView (ListView):
    queryset = product_detail.objects.filter(type_of_product='TA')
    template_name = 'produkty/tablety_list.html'

class LaptopyListView (ListView):
    queryset = product_detail.objects.filter(type_of_product='LA')
    template_name = 'produkty/laptopy_list.html'

class InneListView (ListView):
    queryset = product_detail.objects.filter(type_of_product='IE')
    template_name = 'produkty/inne_list.html'

class Product_detailDetailView (DetailView):
    model = product_detail
