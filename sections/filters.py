import django_filters

from sections.models import Shop


class ShopFilter(django_filters.FilterSet):
    class Meta:
        model = Shop
        fields = ['country']
