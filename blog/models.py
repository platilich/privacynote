from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')

    registered = models.DateTimeField(auto_now_add=True, verbose_name='Зарегистрирован')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Post(models.Model):
    name = models.CharField(max_length=100, verbose_name='Названия')
    description = models.TextField(blank=True, max_length=300, verbose_name='Описание')
    text = models.TextField(blank=False, verbose_name='Текст')


    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='Автор')


    def __str__(self):
        return self.name