from django.contrib import admin
from django.contrib.sites.management import Site
from magic.models import Event , Log


#we really don't need to admin the Site app ( for now)...
admin.site.unregister( Site )

class EventAdmin(admin.ModelAdmin):
    filter_vertical = ('related',)

admin.site.register(Event,EventAdmin)


class LogAdmin(admin.ModelAdmin):
    list_display = ('created','kind','view_log')
    list_filter = ('created','kind')
    search_fields = ('log','kind')
    date_hierarchy = 'created'

admin.site.register(Log,LogAdmin)
