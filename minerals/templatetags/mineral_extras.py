from django import template

register = template.Library()


@register.filter('property_display')
def property_display(property_str):
    """Estimates the # of min to complete a step based on the passed-in wordcount"""
    for_display = property_str.replace('_', ' ')
    return for_display
