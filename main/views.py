import os
from wsgiref.util import FileWrapper

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.encoding import smart_str


def main_index(request):
    return render(request, 'main/index.html')


def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'cmedata', filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404