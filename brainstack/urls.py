from django.conf.urls import patterns, include, url

from core.views import HomeView, SPAView, SPAJoinView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^spa/(?P<project_id>\d+)$', SPAView.as_view(), name='spa'),
    url(r'^spa/(?P<project_hash>\w+)$', SPAJoinView.as_view(), name='spa-join'),
    url(r'^api/', include('api.urls', namespace='api')),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}, name='logout' ),
)
