from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from django.db.models import UniqueConstraint
# from packages
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Sarlavxa")
    content = models.CharField(max_length=1000, verbose_name="Batafsil")
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.CharField(max_length=60, verbose_name="Yuklovchi shaxs")
    viewers = models.ManyToManyField(User, blank=True, verbose_name="Ko'ruvchilar")

    def __str__(self):
        return self.title

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="like bosgan odam")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="qaysi blogga bosilganligi")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['author', 'blog'], name='unique_like')
        ]

    def __str__(self):
        return self.author.username

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="comment bosgan odam")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="qaysi blogga bosilganligi")
    content = models.CharField(max_length=1000, verbose_name="comment")

    def __str__(self):
        return self.author.username + " " + self.content
