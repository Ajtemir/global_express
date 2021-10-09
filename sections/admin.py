from django.contrib import admin

from sections.models import Question, Shop, Country, News, Category, AboutUsInformation, ImagesAboutUs

admin.site.register(Question)
admin.site.register(Shop)
admin.site.register(Country)
admin.site.register(News)
admin.site.register(Category)
admin.site.register(AboutUsInformation)
admin.site.register(ImagesAboutUs)

