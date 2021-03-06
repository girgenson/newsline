from django.db import models
from django.contrib.humanize.templatetags import humanize


class PieceOfNews(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='news', blank=False, null=False)

    class Meta:
        ordering = ('date',)
        verbose_name = 'Piece of news'
        verbose_name_plural = 'News'

    def humanized_date(self):
        return humanize.date(self)

    def __str__(self):
        return self.title
