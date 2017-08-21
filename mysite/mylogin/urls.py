from mylogin.views import *
from django.conf.urls import url,include
urlpatterns = [
        url(r'^test/',testview),
	url(r'^reg/',reg),
]
