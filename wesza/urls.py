from django.conf.urls import patterns, url

from wesza import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/posts.json$', views.posts_json, name='posts_json'),
    url(r'^api/oldapp.json$', views.posts_json, name='oldapp'),
    url(r'^post/(?P<pid>[0-9]+)/$', views.single_post, name="single_post"),
    url(r'^skarb', views.skarb, name='skarb'),
)
