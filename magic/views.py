from django.shortcuts import render_to_response
from django.template import RequestContext
from magic.models import Event

def home(request):
    return render_to_response('magic/home.html',RequestContext(request,{

            }))
