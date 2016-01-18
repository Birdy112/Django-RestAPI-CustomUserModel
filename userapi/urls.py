from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from userapi import views

urlpatterns = patterns('',
    url(r'^api/$', views.UserList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^login/?$', 'userapi.views.obtain_expiring_auth_token'),
    url(r'^retrieve/(?P<pk>[0-9]+)/$', views.UserRetrieve.as_view()),
    )

urlpatterns = format_suffix_patterns(urlpatterns)