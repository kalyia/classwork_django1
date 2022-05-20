from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name="Название", max_length=100)
    description = models.TextField(verbose_name="Описание", max_length=500)
    author = models.CharField(verbose_name="Автор", max_length=100)


class Comment(models.Model):
    user_comment = models.CharField(verbose_name="Комментарий", max_length=100)
    author = models.CharField(verbose_name="Автор", max_length=100)

