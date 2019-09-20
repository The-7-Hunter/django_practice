from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_show_form$', views.new_show_form),
    url(r'^add_new_show', views.add_new_show),

    url(r'^(?P<show_id>\d+)$', views.display_show_info),
    url(r'^(?P<show_id>\d+)/edit$', views.edit_show_form),
    url(r'^(?P<show_id>\d+)/edit_show$', views.edit_show),

    url(r'^(?P<show_id>\d+)/delete$', views.delete_warning),
    url(r'^(?P<show_id>\d+)/delete_show$', views.delete_show),
]