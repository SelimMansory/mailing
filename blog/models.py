from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержание статьи')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    count_view = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    publication = models.DateField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return f'{self.title}, {self.content}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блог'