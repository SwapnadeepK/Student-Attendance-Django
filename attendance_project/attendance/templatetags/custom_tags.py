from django import template

register = template.Library()

@register.filter
def is_teacher(user):
    return user.groups.filter(name='Teachers').exists()
