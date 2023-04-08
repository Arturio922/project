from django.db import models


class Coment(models.Model):
    title = models.CharField('имя', max_length=50)
    full_text = models.TextField('Отзыв')

    def __str__(self):
        return self.title




