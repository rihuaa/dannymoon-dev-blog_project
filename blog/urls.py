from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^blog/(?P<pk>\d+)/$', views.topics, name='topics'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact')
]