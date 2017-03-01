from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.members_list, name='members_list'),
]