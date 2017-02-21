from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.contrib.auth import urls
from .models import Incidents, County
from analysis import views
import analysis


urlpatterns = patterns('',
	url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
	url(r'^incidentData/$', GeoJSONLayerView.as_view(model=Incidents, properties=('list_of_at','casulties')), name='incidentsData'),
	url(r'^countyData/$', GeoJSONLayerView.as_view(model=County, properties=()), name='countyData'),
	url(r'^index/$', analysis.views.index, name='index'),
	url(r'^default/$', analysis.views.default, name='default'),
	url(r'^register/$', analysis.views.register, name='register'),
	url(r'^login/$', analysis.views.user_login, name='login'),
	url(r'^logout/$', analysis.views.user_logout, name='logout'),
)
