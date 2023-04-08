from django.db import models


class User(models.Model):
    email = models.EmailField('e-mail', max_length=50)
    password = models.CharField('Введите пароль', max_length=50)

    def __str__(self):
        return self.email

