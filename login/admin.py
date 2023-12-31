from django.contrib import admin
from .models import Post, AdminBlogs
# Register your models here.
admin.site.register(Post)
admin.site.register(AdminBlogs)