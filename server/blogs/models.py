from django.db import models
from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blog')


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')


class Comment(models.Model):
    content = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')


class Category(models.Model):
    name = models.CharField(max_length=128)


class Tag(models.Model):
    name = models.CharField(max_length=128)


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_categories')


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='post_tags')
