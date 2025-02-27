from django.conf import settings
from django.contrib import admin
from unfold.admin import ModelAdmin
from core.models import Files
from django.utils.safestring import mark_safe


@admin.register(Files)
class FilesAdmin(ModelAdmin):
    readonly_fields = ('file_url', )
    fields = ('file', 'name', 'key', 'file_url')
    search_fields = ('key', 'name')
    list_display = ('name', 'key', 'file_url')

    def file_url(self, obj):
        url = settings.URL_ADMIN + str(obj.key)
        html = f'''
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
            <a href="{url}" target="_blank">{url}</a>
            <button type="button" onclick="copyToClipboard('{url}')" style="margin-left: 10px; margin-right: 5px;">Copy</button>
        </div>
        <script>
        function copyToClipboard(text) {{
            if (navigator.clipboard) {{
                navigator.clipboard.writeText(text)
                    .then(function() {{
                        alert("Link copied!");
                    }})
                    .catch(function(err) {{
                        alert("Error copying: " + err);
                    }});
            }} else {{
                var textArea = document.createElement("textarea");
                textArea.value = text;
                document.body.appendChild(textArea);
                textArea.focus();
                textArea.select();
                try {{
                    document.execCommand("copy");
                    alert("Link copied!");
                }} catch (err) {{
                    alert("Error copying: " + err);
                }}
                document.body.removeChild(textArea);
            }}
        }}
        </script>
        '''
        return mark_safe(html)

    file_url.short_description = 'Generated link'
    file_url.allow_tags = True
