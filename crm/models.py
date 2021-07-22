from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Claim(models.Model):

    STATUS = (('opened', 'открыта'),
              ('in_progress', 'в работе'),
              ('closed', 'закрыта'))

    name = models.CharField(max_length=50,
                            verbose_name='Наименование заявки')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Время создания')
    changed = models.DateTimeField(auto_now=True,
                                   verbose_name='Время изменения')
    category = models.OneToOneField(Category,
                                    on_delete=models.CASCADE,
                                    related_name='bids',
                                    verbose_name='Категория')
    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.CASCADE,
                              related_name='bids',
                              verbose_name='Автор')
    status = models.TextField(choices=STATUS,
                              verbose_name='Статус заявки')

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Список заявок'

    def __str__(self):
        return f'{self.name}'
