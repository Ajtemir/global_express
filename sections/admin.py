from django.contrib import admin

from parcels.models import Parcel
from sections.models import (Question, Shop, Country, News, Category,
                             AboutUsInformation, ImagesAboutUs, HowItWorks,
                             ImagesHowItWorks, FaqSubBlock, FaqBlock)

admin.site.register(Question)
admin.site.register(Shop)
admin.site.register(Country)


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(News, NewsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(AboutUsInformation)
admin.site.register(ImagesAboutUs)
admin.site.register(HowItWorks)
admin.site.register(ImagesHowItWorks)
admin.site.register(FaqBlock)
admin.site.register(FaqSubBlock)


