from django.conf.urls import url
from views import KontaktCreateView

urlpatterns = [
    url(r'^$', KontaktCreateView.as_view(), name='wyslij_kontakt'),
]
