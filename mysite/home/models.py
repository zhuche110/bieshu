#coding=utf8
from __future__ import unicode_literals
from ckeditor.fields import RichTextField


from django.db import models


# Create your models here.
class House(models.Model):
	floor_num_choices= (('1', '一层平房'),('2', '两层别墅'),('3','三层别墅'),('4','四层别墅'),('22','双拼别墅'),('0','不限制'))
	floor_area_choices=(('100', '<100平'),('200', '100-200平'),('300','200-300平'),('400','大于300平'),('0','不限制'))
	title=models.CharField('标题',max_length=100,help_text="文章标题，100字以内")
	content=RichTextField('正文',max_length=10000,)
	floor_num=models.CharField('别墅层数',choices=floor_num_choices,max_length=20)
	floor_area=models.CharField('占地面积',choices=floor_area_choices,max_length=20)
	create_date=models.DateField(auto_now_add=True)
	update_date=models.DateField(auto_now=True)
	
	def __unicode__(self):
		return self.title

class Photo(models.Model):
	if_cover_choices=(('1','是'),('0','否'),)
	house=models.ForeignKey(House)
	images=models.ImageField(upload_to='static/photos')
	title=models.CharField('图片说明',max_length=100,blank=True)
	order=models.CharField('排序标志',max_length=10,default=0)
	if_cover=models.CharField('是否设置为封面图片',max_length=10,choices=if_cover_choices,default='0')
	
	def __unicode__(self):
		return self.title
	
'''
class PhotoInline(admin.TabularInline):
	model = Photo
     
class HouseAdmin(admin.ModelAdmin):
	inlines = [PhotoInline]
'''
