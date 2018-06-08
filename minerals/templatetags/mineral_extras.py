import string
from django import template

register = template.Library()


@register.filter('property_display')
def property_display(property_str):
    """Estimates the # of min to complete a step based on the passed-in wordcount"""
    for_display = property_str.replace('_', ' ')
    return for_display


@register.inclusion_tag('minerals/mineral_initials.html', takes_context=True)
def mineral_initial_list(context):
    """Returns the alphabet to filter minerals by initial"""
    alpha_list = string.ascii_uppercase
    try:
        context['l_selected']
    except Exception:
        initial = 'A'
    else:
        initial = context['l_selected']
    return {'alpha_list': alpha_list, 'l_selected': initial}
