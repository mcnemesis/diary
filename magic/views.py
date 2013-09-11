from django.shortcuts import render_to_response
from django.template import RequestContext
from magic.models import Event
from diary.settings import *

def home(request):
    events = Event.public_stream()
    categories = [{'name' : e.view_kind, 'key' : e.kind } for e in events.distinct('kind')]
    events_dict= {}
    for c in categories:
        events_dict[c['key']] = events.filter( kind = c['key'] )

    return render_to_response('magic/index.html',RequestContext(request,{
            'MAGICIAN_NAME' : MAGICIAN_NAME,
            'title' : HOME_TITLE,
            'description' : SITE_DESCRIPTION,
            'magic' : {
                    'categories' : categories,
                    'events' : events_dict
                }
            }))
