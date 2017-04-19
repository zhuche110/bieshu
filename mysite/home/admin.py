from django.contrib import admin
from home.models import House,Photo
#class PhotoInline(admin.TabularInline):
class PhotoInline(admin.StackedInline):
	model = Photo

class HouseAdmin(admin.ModelAdmin):
	inlines = [PhotoInline]
admin.site.register(House,HouseAdmin)
admin.site.register(Photo)
# Register your models here.
