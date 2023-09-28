from django.contrib import admin
from blog.models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'count_view', 'publication',)
    search_fields = ('title', 'count_view', 'publication',)