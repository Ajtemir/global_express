from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from pytils.translit import slugify

from sections.media_path import shop_icon, shop_image, news_image, about_us_image, how_it_work_image


class Question(models.Model):
    email = models.EmailField(verbose_name=_('Почта'))
    phone = models.CharField(verbose_name=_('Телефон'), max_length=50)
    name = models.CharField(verbose_name=_('Имя'), max_length=50)
    comment = models.CharField(max_length=324, null=True,
                               blank=True, verbose_name=_('Коментарий'))

    class Meta:
        db_table = 'question'
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')

    def __str__(self):
        return self.email


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('название страны'))

    class Meta:
        db_table = 'country'
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
        db_table = 'shop'
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазины')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name=_('название категории новостей'),
                            max_length=50)
    slug = models.SlugField(verbose_name=_('поле slug'), max_length=60,
                            unique=True)

    class Meta:
        db_table = 'category'
        verbose_name = _('категория')
        verbose_name_plural = _('категории')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(verbose_name=_('название'), max_length=50)
    slug = models.SlugField(verbose_name=_('поле slug'), unique=True)
    image = models.ImageField(verbose_name=_('фотография'), upload_to=news_image)
    timestamp = models.DateTimeField(verbose_name=_('дата и время'), blank=True,
                                     auto_now_add=True)
    description = models.TextField(verbose_name=_('описание'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='news', verbose_name=_('категория'))

    class Meta:
        db_table = 'news'
        verbose_name = _('новости')
        verbose_name_plural = _('новости')

    def get_absolute_url(self):
        return reverse('sections:detail-news', kwargs={'slug': self.slug})

    def get_other_news(self):
        return News.objects.exclude(pk=self.pk).order_by('-id')[:3]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class AboutUsInformation(models.Model):
    title = models.CharField(verbose_name=_('название'), max_length=50)
    description = models.TextField(verbose_name=_('описание'))
    video = models.URLField(verbose_name=_('видео'))

    class Meta:
        db_table = 'about_us'
        verbose_name = _('информация о нас')
        verbose_name_plural = _('информация о нас')

    def __str__(self):
        return self.title


class ImagesAboutUs(models.Model):
    image = models.ImageField(verbose_name=_('фотография'),
                              upload_to=about_us_image)
    parent = models.ForeignKey(AboutUsInformation, verbose_name=_('о нас'),
                               on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'images_about_us'
        verbose_name = _('фотография ABOUT_US')
        verbose_name_plural = _('фотографии ABOUT_US')

    def __str__(self):
        return self.parent.title


class HowItWorks(models.Model):
    title = models.CharField(verbose_name=_('название'), max_length=50)
    description = models.TextField(verbose_name=_('описание'))

    class Meta:
        db_table = 'how_it_works'
        verbose_name = _('как это работает')
        verbose_name_plural = _('как это работает')

    def __str__(self):
        return self.title


class ImagesHowItWorks(models.Model):
    image = models.ImageField(verbose_name=_('фотография'),
                              upload_to=how_it_work_image)
    parent = models.ForeignKey(HowItWorks, verbose_name=_('как это работает'),
                               on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'images_how_it_works'
        verbose_name = _('фотография HowItWorks')
        verbose_name_plural = _('фотографии HowItWorks')

    def __str__(self):
        return self.parent.title


class FaqBlock(models.Model):
    title = models.CharField(verbose_name=_('название'), max_length=50)

    class Meta:
        db_table = 'faq_block'
        verbose_name = _('FAQ блок')
        verbose_name_plural = _('FAQ блоки')

    def __str__(self):
        return self.title


class FaqSubBlock(models.Model):
    title = models.CharField(verbose_name=_('название'), max_length=50)
    description = models.TextField(verbose_name=_('описание'))
    parent_block = models.ForeignKey(FaqBlock, verbose_name=_('родительский блок'),
                                     on_delete=models.CASCADE, related_name='sub_blocks')

    class Meta:
        db_table = 'faq_sub_block'
        verbose_name = _('FAQ подблок')
        verbose_name_plural = _('FAQ подблоки')

    def __str__(self):
        return self.parent_block.title

