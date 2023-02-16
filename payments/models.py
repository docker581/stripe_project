from django.db import models

CURRENCIES = (
    ('usd', 'usd'),
    ('eur', 'eur'),
)


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Стоимость')
    currency = models.CharField(max_length=127, choices=CURRENCIES, verbose_name='Валюта')

    class Meta:
        verbose_name = 'Единица товара'
        verbose_name_plural = 'Единицы товара'

    def __str__(self):
        return f'Товар {self.name}'


class Order(models.Model):
    currency = models.CharField(max_length=127, choices=CURRENCIES, verbose_name='Валюта')
    items = models.ManyToManyField(to=Item, verbose_name='Товары')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ № {self.id}'
