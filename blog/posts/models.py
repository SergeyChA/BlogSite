from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})


class Comments(models.Model):
    text = models.CharField('текст комментария', max_length=200)
    pub_date = models.DateTimeField('дата публикации', default=timezone.now)
    post = models.ForeignKey(Posts, verbose_name='пост', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='автор', max_length=20, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.post_id})
