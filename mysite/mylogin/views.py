from django.shortcuts import render
from django.http import HttpResponse 
from mylogin.models import MyloginForm,MyRegForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect 
import json

def testview(request):
	#print dir(request)
	#return HttpResponse("Text only, please.", content_type="text/plain")
	#f=MyloginForm()
	f=MyRegForm()
	context={'form':f}
	return render(request,'mylogin/mylogin.html',context)
	#return HttpResponse(f)

def login(request):
	f=MyloginForm()
	return HttpResponse(f)
'''
def reg(request):
	if request.method=='GET':
		f=MyRegForm()
		context={'form':f}
		return render(request,'mylogin/reg.html',context)
	else:
		f=MyRegForm(request.POST)
		if f.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			user = User.objects.create_user(username=username,password=password)
			
			return  HttpResponseRedirect('/')
		else:
			context={'form':f}
			return render(request,'mylogin/reg.html',context)
'''

def reg(request):
	if request.method=='GET':
		f=MyRegForm()
		context={'form':f}
		return render(request,'mylogin/reg.html',context)
	else:
		data = {"retcode": "0","msg":"success"}
		return HttpResponse(json.dumps(data))


# Create your views here.
