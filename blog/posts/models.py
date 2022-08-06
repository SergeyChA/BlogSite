from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField('заголовок', max_length=50)
    text = models.TextField('текст')
    pub_date = models.DateTimeField('дата публикации', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='автор', max_length=20, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title