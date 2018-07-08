from django import template


register = template.Library()

@register.simple_tag
def b(text):
    if not text or text == 'None':
        return "N/I"
    return text.replace('-',' ')
