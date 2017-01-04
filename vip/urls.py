
from django.conf.urls import url, include
from django.contrib import admin
from views import HomeTemplateView, SkupSrebraTemplateView, SkupZlotaTemplateView, ONasTemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', HomeTemplateView.as_view(), name='home_page'),
    url(r'^produkty/', include('produkty.urls', namespace='produkty')),
    url(r'^skup_zlota/', SkupZlotaTemplateView.as_view(), name='skup_zlota'),
    url(r'^skup_srebra/', SkupSrebraTemplateView.as_view(), name='skup_srebra'),
    url(r'^o_nas/', ONasTemplateView.as_view(), name='o_nas'),
    url(r'^kontakt/', include('formularz_kontaktowy.urls', namespace='kontakt')),
    url(r'^opinie/', include('opinie.urls', namespace='opinie')),
    url(r'^admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
