from django.conf.urls import url
from . import views
                
urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.new),
    url(r'^shows/add$', views.showsAdd),
    url(r'^shows/(?P<showID>\d+)$', views.desc),
    url(r'^shows/(?P<showID>\d+)/destroy$', views.destroy),
    url(r'^shows/(?P<showID>\d+)/edit$', views.edit),
    url(r'^shows/(?P<showID>\d+)/editShow$', views.editShow),
]