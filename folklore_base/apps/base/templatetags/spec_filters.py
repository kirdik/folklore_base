from django import template
from folklore_base.apps.base.models import *
import re

register = template.Library()

@register.simple_tag()
def locate_tag():
    return Oblast.objects.all()

@register.simple_tag()
def reestr_tag(id_of_seance):
    # return Reestr.objects.all()
    return Reestr.objects.select_related().filter(seans=id_of_seance)

@register.filter()
def req_filt(url_in):
    i = re.search(r"\d+$", url_in)
    return i.group(0)
@register.filter()
def clean_id(str_in):
    rres = re.sub(r'\W', '', str_in)
    return rres