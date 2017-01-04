# coding: utf-8

from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from models import product_detail
from django.db.models import Q


class Product_detailListView (ListView):
    model = product_detail
    queryset = product_detail.objects.all()
    def get(self, request):
        query = request.GET.get("q")
        product_detail.objects.filter(
        Q(name__icontains=query)|
        Q(producent__icontains=query)|
        Q(type_of_product__icontains=query) |
        Q(description__icontains=query)
        ).distinct()

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