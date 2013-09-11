from django import template

register = template.Library()

@register.filter
def get(h, key):
    try:
        return h.get(key,'')
    except:
        return ''
