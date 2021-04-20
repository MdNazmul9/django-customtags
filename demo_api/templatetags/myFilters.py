from  django import template
from datetime import datetime

register = template.Library()
def cutlast(value, elements):
    return value[:len(value) - elements] + "Nazmul Hossain"
@register.simple_tag
def printdt(format):
    return datetime.now().strftime(format)

register.filter("myCut", cutlast)