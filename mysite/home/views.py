#coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from home.models import House,Photo
# Create your views here.
def index(request):
	PAGENUM=3
	house_list=House.objects.all()	
	photo_list=Photo.objects.all()
	context={'house_list':house_list,'photo_list':photo_list}
	return render(request,"home/house_list.html",context)
	
	#return HttpResponse('hello world')
def house_detail(request,house_id):
	house=House.objects.get(pk=house_id)
	photo_list=Photo.objects.filter(house=house_id).order_by('order')
	context={'house_detail':house,'photo_list':photo_list}
	return render(request,"home/house_detail.html",context)
