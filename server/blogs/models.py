from django.db import models
from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blog')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return self.user


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_categories')

    def __str__(self):
        return f"{self.post} : {self.category}"


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='post_tags')

    def __str__(self):
        return f"{self.post} : {self.tag}"
