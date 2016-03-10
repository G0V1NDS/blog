from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

# Create your models here.
class Post(models.Model):
    post_title=models.CharField(max_length=100)
    post_content=models.TextField(max_length=2000)
    post_pub_date=models.DateField('Date Published')

    def __str__(self):
        return self.post_title

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_user=models.CharField(max_length=100)
    comment_content=models.TextField(max_length=100)
    comment_date=models.DateField('Date Commented')
    def __str__(self):
        return self.comment_content

admin.site.register(Post)
admin.site.register(Comment)