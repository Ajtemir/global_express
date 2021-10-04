from django.db import models
from django.utils.translation import ugettext_lazy as _


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



