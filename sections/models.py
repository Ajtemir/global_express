from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from sections.media_path import shop_icon, shop_image, news_image


class Question(models.Model):
    email = models.EmailField(verbose_name=_('Почта'))
    phone = models.CharField(verbose_name=_('Телефон'), max_length=50)
    name = models.CharField(verbose_name=_('Имя'), max_length=50)
    comment = models.CharField(max_length=324, null=True,
                               blank=True, verbose_name=_('Коментарий'))

    class Meta:
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')

    def __str__(self):
        return self.email


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('название страны'))

    class Meta:
        verbose_name = _('страна')
        verbose_name_plural = _('страны')

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("название"))
    description = models.TextField(verbose_name=_("описание"))
    url = models.URLField(verbose_name=_("url"))
    image = models.ImageField(verbose_name=_("фотография"),
                              upload_to=shop_image)
    icon = models.ImageField(verbose_name=_("иконка"), unique=True,
                             upload_to=shop_icon)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
                                related_name='shops', verbose_name=_('страна'))

    class Meta:
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазины')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name=_('название категории новостей'),
                            max_length=50)

    class Meta:
        verbose_name = _('категория')
        verbose_name_plural = _('категории')

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(verbose_name=_('название'), max_length=50)
    image = models.ImageField(verbose_name=_('фотография'), upload_to=news_image)
    timestamp = models.DateTimeField(verbose_name=_('дата и время'), blank=True,
                                     auto_now_add=True)
    description = models.TextField(verbose_name=_('описание'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='news', verbose_name=_('категория'))

    class Meta:
        verbose_name = _('новости')
        verbose_name_plural = _('новости')

    def get_absolute_url(self):
        return reverse('sections:detail-news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
