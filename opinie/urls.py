from django.conf.urls import url
from views import OpiniaCreateView, OpiniaListView

urlpatterns = [
    url(r'^$', OpiniaListView.as_view(), name='lista_opini'),
    url(r'^dodaj/$', OpiniaCreateView.as_view(), name='dodaj_opinie'),
]
