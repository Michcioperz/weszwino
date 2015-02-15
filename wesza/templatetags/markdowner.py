from django import template
from markdown import markdown

register = template.Library()

@register.filter
def markdowner(text):
    return markdown(text)
