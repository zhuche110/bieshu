#coding=utf8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.forms import ModelForm
# Create your models here.

class MyloginForm(forms.Form):
	username=forms.CharField(max_length=50,min_length=6,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'}))
	password=forms.CharField(max_length=50,min_length=6,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码'}))


class MyRegForm(ModelForm):
	username=forms.CharField(max_length=50,min_length=6,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'请输入用户名'}))
	password=forms.CharField(max_length=50,min_length=6,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'请输入密码'}))
	class Meta:
		fields=['username','password']
		model=User
