from django.contrib import admin

# Register your models here.
from .models import UserAva

class UserAvaAdmin(admin.ModelAdmin):
    model = UserAva
    list_display = ['id','ava','updated_at']

admin.site.register(UserAva,UserAvaAdmin)