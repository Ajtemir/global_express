import django_filters

from sections.models import Shop, News


class ShopFilter(django_filters.FilterSet):
    class Meta:
        model = Shop
        fields = ['country']


class NewsFilter(django_filters.FilterSet):
    class Meta:
        model = News
        fields = ['category']
