from django.contrib import admin
from .models import Region, RspsDiv, RspsMember

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name','middle_name', 'last_name', 'job', 'rsps_div')
admin.site.register(Region)
admin.site.register(RspsDiv)
admin.site.register(RspsMember, MemberAdmin)
