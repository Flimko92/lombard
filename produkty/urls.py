# coding: utf-8
from django.conf.urls import url
from views import (Product_detailListView, Product_detailDetailView, BizuteriaListView, TelefonyListView,
                   TabletyListView, LaptopyListView, InneListView, Product_detailCreateView, Product_detailDeleteView,
                   Product_detailUpdateView
                  )

urlpatterns = [

    url(r'^product_detail_list/$', Product_detailListView.as_view(), name='product_detail_list'),
    url(r'^product_detail_list/add/$', Product_detailCreateView.as_view(), name='product_detail_add'),
    url(r'product_detail_list/update/(?P<pk>\d+)/$', Product_detailUpdateView.as_view(), name='product_detail_update'),
    url(r'product_detail_list/delete/(?P<pk>\d+)/$', Product_detailDeleteView.as_view(), name='product_detail_delete'),
    url(r'^bizuteria_list/$', BizuteriaListView.as_view(), name='bizuteria_list'),
    url(r'^telefony_list/$', TelefonyListView.as_view(), name='telefony_list'),
    url(r'^tablety_list/$', TabletyListView.as_view(), name='tablety_list'),
    url(r'^laptopy_list/$', LaptopyListView.as_view(), name='laptopy_list'),
    url(r'^inne_list/$', InneListView.as_view(), name='inne_list'),
    url(r'^product_detail_list/(?P<pk>\d+)/$', Product_detailDetailView.as_view(), name='product_detail_detail'),
]