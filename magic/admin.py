from django.contrib import admin
from django.contrib.sites.management import Site
from magic.models import Event


#we really don't need to admin the Site app ( for now)...
admin.site.unregister( Site )

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event,EventAdmin)
