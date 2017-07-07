import os, tempfile, zipfile
from django.http import HttpResponse
from django.core.servers.basehttp import *

def send_file(request):
    """
    Send a file through Django without loading the whole file into
    memory at once. The FileWrapper will turn the file object into an
    iterator for chunks of 8KB.
    """
    filename = __file__ # Select your file here.
    # wrapper = FileWrapper(file(filename))
    wrapper = FileWrapper(open(filename))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    return response