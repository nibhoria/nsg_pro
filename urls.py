from django.conf.urls import url 
from . import views


urlpatterns = [
    url(r'^$', views.issued_list, name = 'issued_list'),
    url(r'^return_form/$', views.return_form, name = 'return_form'),
    url(r'^delet/(?P<x>.+)/$',views.delet, name='delet'),
 ]
