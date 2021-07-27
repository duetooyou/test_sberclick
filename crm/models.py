from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from model_utils import FieldTracker


class Client(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name='Имя пользователя')
    surname = models.CharField(max_length=40,
                               verbose_name='Фамилия пользователя')
    notification = models.BooleanField(default=False,
                                       verbose_name='Уведомления')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Список категорий'

    def __str__(self):
        return f'{self.name}'


class Claim(models.Model):
    STATUS = (('открыта', 'Открыта'),
              ('в работе', 'В работе'),
              ('закрыта', 'Закрыта'))

    name = models.CharField(max_length=50,
                            verbose_name='Наименование заявки',
                            )
    created = models.DateField(auto_now_add=True,
                               verbose_name='Время создания')
    changed = models.DateTimeField(auto_now=True,
                                   verbose_name='Время изменения')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='categories',
                                 verbose_name='Категория')
    body = models.TextField(max_length=400,
                            verbose_name='Содержание')
    owner = models.ForeignKey(Client,
                              on_delete=models.CASCADE,
                              related_name='clients',
                              verbose_name='Автор заявки')
    executor = models.ForeignKey(get_user_model(),
                                 on_delete=models.CASCADE,
                                 related_name='executors',
                                 verbose_name='Исполнитель заявки')
    status = models.TextField(choices=STATUS,
                              verbose_name='Статус заявки')
    slug = models.SlugField(max_length=150,
                            unique=True,
                            )
    tracker = FieldTracker()

    class Meta:
        unique_together = ('name', 'category', 'owner')
        ordering = ('created',)
        verbose_name = 'Заявки'
        verbose_name_plural = 'Список заявок'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('claims_detail', kwargs={'slug': self.slug})
