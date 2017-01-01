from django.template import Library

register = Library()

@register.inclusion_tag('tags/show_shots.html')
def show_shots(obj):
    return {'shots': obj.shots.all()}