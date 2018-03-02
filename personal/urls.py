from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout,login


urlpatterns=[
	url(r'^login/$',login,name = 'login'),
	url(r'^$',views.index,name='index'),
	url(r'^logout/$',logout,name = 'logout'),
	url(r'^contact',views.contact,name='contact')]