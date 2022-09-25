from django.contrib import admin

from . import models


class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'category', 'add_time')

class AdminComment(admin.ModelAdmin):
    list_display = ('news', 'email', 'comment', 'status')

admin.site.register(models.Category)
admin.site.register(models.News, AdminNews)
admin.site.register(models.Comment, AdminComment)