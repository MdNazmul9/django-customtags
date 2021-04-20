from  django import template

register = template.Library()

def cutlast(value, elements):
    return value[:len(value) - elements] + "Nazmul Hossain"

register.filter("myCut", cutlast)