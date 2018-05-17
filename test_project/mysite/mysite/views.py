from django.http import HttpResponse
from django.http import Http404, HttpResponse
import datetime
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404(offset)
    now = datetime.datetime.now()
    dt = now + datetime.timedelta(hours=offset)
    return render(request, 'current_datetime.html',{'current_datetime':now})
    return HttpResponse(html)



