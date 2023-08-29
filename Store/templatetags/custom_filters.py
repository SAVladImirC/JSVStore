from django import template

register = template.Library()

@register.filter
def get_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

@register.filter
def mul(itm1, itm2):
    return itm1 * itm2