from django.contrib import admin
from stores.models import *

class UserProfileAdmin(admin.ModelAdmin):
	fieldsets = [
	('Created By',{'fields':['creator']}),
	('User Info',{'fields':['user','address','phone','country']}),
	]

	list_display = ('__str__','address','phone')
	#search_fields = ['user']

class AddressAdmin(admin.ModelAdmin):
	list_display = ('__str__',)

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Color)
admin.site.register(CartList)
