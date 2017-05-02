from home.views import *
from django.conf.urls import url
urlpatterns =[
	url(r'^$',index),
	url(r'house_list',index),
	url(r'house_detail/(?P<house_id>[0-9]+)/$',house_detail)

]
