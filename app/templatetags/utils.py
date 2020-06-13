from django import template
import re
register=template.Library()

@register.filter
def get_type(value):
	t=re.search("'.*'",str(type(value)))
	return t.group(0).replace("'","")

@register.filter(name='times') 
def times(number):
    return range(number)

@register.simple_tag
def update_serial(value):
    """Allows to update existing variable in template"""
    return value