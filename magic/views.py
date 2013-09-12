from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q

from magic.models import Event
from diary.settings import *

def home(request):
    events = Event.public_stream() if not request.user.is_authenticated() else Event.stream()

    if 'search' in request.REQUEST:
        '''
        eventually, searching should be done the proper way - using a search-engine like solr or haystack
        But for now...
        '''
        query = request.REQUEST['search']
        try:
            '''test'''
            Event.objects.filter(title__search = '.').exists()

            events = events.filter(
                    Q(title__search = query) |
                    Q(summary__search = query) |
                    Q(tags__search = query) |
                    Q(purpose__search = query) |
                    Q(details__search = query) |
                    Q(partners__search = query) |
                    Q(place__search = query)
                    )
        except NotImplementedError:
            '''True, Full-Text search is only supported in Django for MySQL for now'''
            events = events.filter(
                    Q(title__icontains = query) |
                    Q(summary__icontains = query) |
                    Q(tags__icontains = query) |
                    Q(purpose__icontains = query) |
                    Q(details__icontains = query) |
                    Q(partners__icontains = query) |
                    Q(place__icontains = query)
                    )

    categories = [{'name' : e.view_kind, 'key' : e.kind } for e in events.distinct('kind')]

    events = events.order_by("-created","-date","-time")

    events_dict= {}
    for c in categories:
        events_dict[c['key']] = events.filter( kind = c['key'] )

    return render_to_response('magic/index.html',RequestContext(request,{
            'MAGICIAN_NAME' : MAGICIAN_NAME,
            'title' : HOME_TITLE,
            'description' : SITE_DESCRIPTION,
            'search' : request.REQUEST.get('search',''),
            'magic' : {
                    'categories' : categories,
                    'events' : events_dict
                }
            }))
