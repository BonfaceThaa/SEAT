from django.contrib.gis import admin
from .models import County, Incidents, UserProfile


class IncidentsAdmin(admin.OSMGeoAdmin):
	list_display = ['list_of_at', 'casulties']

admin.site.register(County, admin.OSMGeoAdmin)
admin.site.register(Incidents, admin.OSMGeoAdmin)
admin.site.register(UserProfile)
