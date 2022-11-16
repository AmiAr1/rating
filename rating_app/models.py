from django.db import models
from rest_framework.authtoken.admin import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    image = models.ImageField(upload_to='', null=True)
    title = models.CharField(
        max_length=100, null=True, blank=False, verbose_name='Название'
    )
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(max_length=20, null=True, blank=True, verbose_name='цена')
    cpu = models.CharField(max_length=50, null=True, blank=False)
    main_camera = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='основная камера'
    )
    front_camera = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='фронтальная камера'
    )
    memory = models.PositiveIntegerField(null=True, blank=False, verbose_name='память')
    ram = models.PositiveIntegerField(null=True, blank=False, verbose_name='оперативная память')
    is_active = models.BooleanField(default=True)
    is_hit = models.BooleanField(default=True)


    def __str__(self):
        return self.title



class Rating(models.Model):
    '''
    Модель рейтинга
    '''
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='ratings',
                             verbose_name='Владелец рейтинга'
                             )
    product = models.ForeignKey(Product,
                                on_delete=models.Model,
                                related_name='ratings',
                                verbose_name='Продукт')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)],
        default=1
    )

    def __str__(self):
        return f'{self.product} - {self.rating}'
