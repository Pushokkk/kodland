from django.db import models
from django.urls import reverse


class Post(models.Model):
    """Пост – небольшая статья на сайте с изображением"""
    title = models.CharField(max_length=200, verbose_name="Название поста")
    text = models.TextField(verbose_name="Основной текст поста")
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/post_images", verbose_name="Иллюстрация поста")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={"pk": self.pk})
