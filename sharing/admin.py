from django.contrib import admin
from .models import AppUser,HelpRequest
# Register your models here.
@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display=('user','first_name','last_name')


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display=('request_by','address','pin_code','country','latitude','longitude','accuracy_meters','altitude_meters','created_at')
