from django.contrib import admin
from .models import *


class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_solved')


admin.site.register(Contact, AdminContact)
