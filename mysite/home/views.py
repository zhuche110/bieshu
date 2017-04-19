#coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from home.models import House
# Create your views here.
def index(request):
	PAGENUM=3
	house_list=House.objects.all()	
	context={'house_list':house_list}
	return render(request,"home/house_list.html",context)
	
	#return HttpResponse('hello world')
