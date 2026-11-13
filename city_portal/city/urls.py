from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^news(?:/.*)?$', views.news, name='news'),
    re_path(r'^management(?:/.*)?$', views.management, name='management'),
    re_path(r'^facts(?:/.*)?$', views.facts, name='facts'),
    re_path(r'^contacts(?:/.*)?$', views.contacts, name='contacts'),
    re_path(r'^history/people/?$', views.history_people, name='history_people'),
    re_path(r'^history/photos/?$', views.history_photos, name='history_photos'),
    re_path(r'^history(?:/.*)?$', views.history, name='history'),
]
