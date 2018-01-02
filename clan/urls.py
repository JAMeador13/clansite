from django.conf.urls import url, handler404, handler500
from . import views

app_name = 'clan'

handler404 = 'clansite.views.handler404'
handler500 = 'clansite.views.handler500'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^streams/Multi-Stream/$', views.multi_stream, name='multistream'),

    url(r'^streams/Multi-Stream/(.+)?/(.+)?/(.+)?/(.+)?/$', views.multi_stream, name='multistream'),

    url(r'^streams/(.+)/$', views.streams, name='streams'),

    url(r'^league/$', views.league, name='league'),

    url(r'^league/season-(?P<num>\d{1})/(?P<tab>teams|record|schedule|compare)?/?$', views.season, name='season'),

    url(r'^stats/$', views.stats, name='stats'),

    url(r'^about/$', views.about, name='about'),
]