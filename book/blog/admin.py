from django.contrib import admin

# Register your models here.
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ['title']


admin.site.register(Blog, BlogAdmin)
