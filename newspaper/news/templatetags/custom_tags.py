from datetime import datetime
from django import template


register = template.Library()

@register.simple_tag()
def date_create(format_string='%d %m %Y'):
    return datetime.utcnow().strftime(format_string)