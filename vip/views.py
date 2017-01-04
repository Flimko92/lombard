# coding: utf-8
from django.views.generic import TemplateView

class HomeTemplateView (TemplateView):
    template_name = 'home.html'

class SkupZlotaTemplateView (TemplateView):
    template_name = 'skup_zlota.html'

class SkupSrebraTemplateView (TemplateView):
    template_name = 'skup_srebra.html'

class ONasTemplateView (TemplateView):
    template_name = 'o_nas.html'