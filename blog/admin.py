from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('title', 'author', 'publication_date')
    search_fields = ('title', 'author', 'publication_date')
    ordering = ('title', 'publication_date')
