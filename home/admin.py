from django.contrib import admin
from .models import *


class AdminArticles(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')


class AdminAuthors(admin.ModelAdmin):
    list_display = ('name', 'image', 'sm')


class AdminComments(admin.ModelAdmin):
    list_display = ('article', 'name', 'created_at')


admin.site.register(Tags)
admin.site.register(Categories)
admin.site.register(Regions)
admin.site.register(Authors, AdminAuthors)
admin.site.register(Articles, AdminArticles)
admin.site.register(Comments, AdminComments)
