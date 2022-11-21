from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'photo_big')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create',)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'price2')
    list_display_links = ('id', 'title')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(BlogModel, BlogAdmin)
admin.site.register(ServicesModel, ServicesAdmin)
admin.site.register(FeedbackModel, FeedbackAdmin)
admin.site.register(PortfolioModel, PortfolioAdmin)



