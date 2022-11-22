from django.contrib import admin
from news.models import Guruxlash, Post
# Register your models here.

@admin.register(Guruxlash)
class GuruxlashAdmin(admin.ModelAdmin):
    list_display = ['ism', 'slug']
    prepopulated_fields = {'slug':['ism',]}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['sarlovha', 'slug']
    prepopulated_fields = {'slug':['sarlovha',]}
