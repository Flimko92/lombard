# coding: utf-8
from django.conf.urls import url
from views import (Product_detailListView, Product_detailDetailView, BizuteriaListView)
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^product_detail_list/$', Product_detailListView.as_view(), name='product_detail_list'),
    url(r'^bizuteria_list/$', BizuteriaListView.as_view(), name='bizuteria_list'),
    url(r'^product_detail_list/(?P<pk>\d+)/$', Product_detailDetailView.as_view(), name='product_detail_detail'),
]