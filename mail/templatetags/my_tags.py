from django import template

register = template.Library()

@register.simple_tag(name='mediapath')
def media_tag():
    return f'/media/'