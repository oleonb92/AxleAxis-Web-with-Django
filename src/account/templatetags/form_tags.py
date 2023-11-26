# account/templatetags/form_tags.py

from django import template
from django.forms.widgets import Widget

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    if isinstance(value, Widget):
        return value.as_widget(attrs={'class': css_class})
    else:
        return value

