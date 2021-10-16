from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Parcel(models.Model):
    timestamp = models.DateField(verbose_name=_('дата создания товара'), auto_now_add=True)

    user = models.ForeignKey(User, verbose_name=_('аккаунт заказчика'),
                             related_name='parcels', on_delete=models.CASCADE)
    recipient = models.CharField(verbose_name=_('получатель Ф.И.О'), max_length=100)
    name = models.CharField(verbose_name=_('наименование товара'), max_length=100)
    amount = models.PositiveIntegerField(verbose_name=_('количество'), default=1)
    price = models.DecimalField(verbose_name=_('общая цена'), decimal_places=2, max_digits=7,
                                default=0.00, validators=[MinValueValidator(Decimal('0.01'))])
    weight = models.DecimalField(verbose_name=_('вес'), decimal_places=2,
                                 max_digits=7, default=0)
    store = models.CharField(verbose_name=_('страна склада'), max_length=50)
    track = models.CharField(verbose_name=_('трек номер'), max_length=18, unique=True)

    IN_PROCESS = 1
    SORTING = 2
    PROCESSED = 3
    RAISED = 4
    FLYING = 5
    SEARCHING = 6
    STORE = 7
    STORE_KG = 8
    UNREGISTERED = 9
    STATUS_CHOICES = (
        (IN_PROCESS, _('В процессе')),
        (SORTING, _('Сортировка')),
        (PROCESSED, _('Обработан')),
        (RAISED, _('Выдан')),
        (FLYING, _('В пути')),
        (SEARCHING, _('В поиске')),
        (STORE, _('На складе')),
        (STORE_KG, _('На складе в KG')),
        (UNREGISTERED, _('Незарегистрированный заказ')),
    )
    status = models.PositiveIntegerField(verbose_name=_('статус'), choices=STATUS_CHOICES,
                                         default=UNREGISTERED)

    is_deleted = models.BooleanField(verbose_name=_('удален'), default=False)
    type = models.CharField(verbose_name=_('вид товара'), max_length=50)
    site = models.URLField(verbose_name=_('веб-сайт'))
    comment = models.TextField(max_length=324, verbose_name=_('коментарии'),
                               blank=True, null=True)
    is_bought_self = models.BooleanField(verbose_name=_('товар куплен клиентом'), default=True)

    class Meta:
        db_table = 'parcels'
        verbose_name = _('посылка')
        verbose_name_plural = _('посылки')

    def __str__(self):
        return self.name
