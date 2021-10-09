from django.contrib import admin

from sections.models import Question, Shop, Country, News, Category

admin.site.register(Question)
admin.site.register(Shop)
admin.site.register(Country)
admin.site.register(News)
admin.site.register(Category)
