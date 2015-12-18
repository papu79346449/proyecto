from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.Form_event),
    url(r'^evento/(?P<pk>[0-9]+)/$', views.evento_detail),
    url(r'^evento/new/$', views.evento_new, name='evento_new'),
]
