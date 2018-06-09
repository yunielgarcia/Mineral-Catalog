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


@register.inclusion_tag('minerals/mineral_groups.html', takes_context=True)
def mineral_groups_list(context):
    """Passes the template a list of groups to filter by"""
    group_list = ['Silicates',
                  'Oxides',
                  'Sulfates',
                  'Sulfides',
                  'Carbonates',
                  'Halides',
                  'Sulfosalts',
                  'Phosphates',
                  'Borates',
                  'Organic_Minerals',
                  'Arsenates',
                  'Native_Elements',
                  'Other']

    try:
        context['g_selected']
    except Exception:
        g_selected = ''
    else:
        g_selected = context['g_selected']
    return {'group_list': group_list, 'g_selected': g_selected}
