from django.db import models
from django.urls import reverse


class ServicesModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=100, verbose_name='Цена')
    price2 = models.CharField(max_length=100, blank=True, verbose_name='Цена доп')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


class FeedbackModel(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m", verbose_name="Фото")

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class BlogModel(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Содержание")
    photo = models.ImageField(upload_to="photos/%Y/%m", verbose_name="Фото для карточки: 250*200")
    photo_big = models.ImageField(upload_to="photos_big/%Y/%m", verbose_name="Фото большое: высота 600")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['time_create', 'title']


class PortfolioModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Раздел')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo_1 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №1')
    photo_2 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №2')
    photo_3 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №3')
    photo_4 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №4')
    photo_5 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №5')
    photo_6 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True,verbose_name='фото №6')
    photo_7 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True,verbose_name='фото №7')
    photo_8 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True,verbose_name='фото №8')
    photo_9 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True,verbose_name='фото №9')
    photo_10 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True,verbose_name='фото №10')
    photo_11 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №11')
    photo_12 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №12')
    photo_13 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №13')
    photo_14 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №14')
    photo_15 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №15')
    photo_16 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", blank=True, verbose_name='фото №16')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"




