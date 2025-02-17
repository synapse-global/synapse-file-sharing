from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Files
from urllib.parse import quote
import mimetypes

def get_file(request, key):
    file = get_object_or_404(Files, key=key)
    mime_type, _ = mimetypes.guess_type(file.file.name)
    response = HttpResponse(file.file, content_type=mime_type)
    response['Content-Disposition'] = f'inline; filename="{quote(file.file.name)}"'
    return response