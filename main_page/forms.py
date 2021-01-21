from django.db import models
from django.urls import reverse


class PaginationMode(models.Model):
    name = models.IntegerField()

    def change_pagination(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name
