from django.shortcuts import render_to_response
from django.template import RequestContext
from magic.models import Event
from diary.settings import *

def home(request):
    return render_to_response('magic/index.html',RequestContext(request,{
            'MAGICIAN_NAME' : MAGICIAN_NAME,
            'title' : HOME_TITLE,
            'description' : SITE_DESCRIPTION
            }))
