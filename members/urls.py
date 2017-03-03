from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.members_list, name='members_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.member_detail, name='member_detail'), 
    url(r'^member/new/$', views.member_new, name='member_new'),
]
