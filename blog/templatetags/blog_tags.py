from django import template

register = template.Library()

@register.simple_tag
def function(a):
    return a+2