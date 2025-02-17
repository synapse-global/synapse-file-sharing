from django.conf import settings
from django.contrib import admin
from unfold.admin import ModelAdmin
from core.models import Files
from django.utils.safestring import mark_safe


@admin.register(Files)
class FilesAdmin(ModelAdmin):
    readonly_fields = ('file_url', )
    fields = ('file', 'key', 'file_url')
    search_fields = ('key', )
    list_display = ('key', 'file_url')

    def file_url(self, obj):
        url = settings.URL_ADMIN + str(obj.key)
        return mark_safe(f'<a href="{url}" target="_blank"> {url} </a>')

    file_url.short_description = 'Сгенерированная ссылка'
    file_url.allow_tags = True
