from django.conf.urls import url
from . import views

app_name = 'dictajaxapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getdict', views.getdict, name='getdict'),
    url(r'^(?P<dict_id>[0-9]+)/$', views.viewdict, name='viewdict'),
    url(r'^create', views.createdict, name='createdict'),
    url(r'^delete', views.deletedict, name='deletedict')
]
