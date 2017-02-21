from django.contrib import admin
from .models import Region, RspsDiv, RspsMember, RspsEvents

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','middle_name', 'job', 'rsps_div')

class RspsDivAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'telephone', 'email')
class RspsEventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'place', 'date', 'rsps_div')
admin.site.register(Region)
admin.site.register(RspsDiv, RspsDivAdmin)
admin.site.register(RspsMember, MemberAdmin)
admin.site.register(RspsEvents, RspsEventsAdmin)
