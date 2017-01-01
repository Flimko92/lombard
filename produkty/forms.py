# coding: utf-8


from django import forms
from models import product_detail, rtv, bizuteria, inne,


class SceneForm(forms.ModelForm):
    class Meta:
        model = scene
        fields = ['movie_title', 'scene_number', 'place', 'place_name', 'time_of_day', ]

class ShotForm(forms.ModelForm):
    class Meta:
        model = shot
        fields = ['scene_number', 'nr_ujecia', 'plan', 'typ_ujecia', 'storyboard', 'opis_ujecia', 'fragment_scenariusza' ]