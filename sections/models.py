from django.db import models
from django.utils.translation import ugettext_lazy as _

from sections.media_path import shop_icon, shop_image


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
