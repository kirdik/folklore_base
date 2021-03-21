from django import template
from folklore_base.apps.base.models import *

register = template.Library()

@register.simple_tag()
def locate():
    return Oblast.objects.all()
