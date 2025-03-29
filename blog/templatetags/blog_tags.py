from django import template

register = template.Library()

@register.filter()
def media_filter(photo):
    if photo and hasattr(photo, 'url'):
        return photo.url  # Возвращаем полный URL к изображению
    return "#"