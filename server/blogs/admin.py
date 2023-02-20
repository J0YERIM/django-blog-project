from django.contrib import admin
from .models import Blog, Post, Comment, Like, Category, Tag, PostCategory, PostTag

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PostCategory)
admin.site.register(PostTag)

