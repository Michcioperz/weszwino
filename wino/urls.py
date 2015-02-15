from django.conf.urls import patterns, url

from wino import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pid>[0-9]+)/$', views.single_post, name="single_post"),
    url(r'^addkom/(?P<pid>[0-9]+)/$', views.addkomm, name="addkomm"),
)
