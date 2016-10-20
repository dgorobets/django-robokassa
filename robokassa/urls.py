#coding: utf-8
try:
    from django.conf.urls.defaults import patterns, url
except ImportError:
    from django.conf.urls import patterns, url

from robokassa import views
    

urlpatterns = [
    url(
          r'^result/$',
          views.receive_result,
          name='robokassa_result'
    ),
    url(
          r'^success/$',
          views.success,
          name='robokassa_success'
    ),
    url(
          r'^fail/$',
          views.fail,
          name='robokassa_fail'
    ),
]

