from django.db import models

class Genre(models.Model):
    name = models.CharField(verbose_name="Название жанра", max_length=50, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    content = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='posts', verbose_name="Жанр")
    image = models.ImageField(verbose_name="Изображение", upload_to='images/', null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title