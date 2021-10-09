from django.contrib import admin

from sections.models import (Question, Shop, Country, News, Category,
                             AboutUsInformation, ImagesAboutUs, HowItWorks,
                             ImagesHowItWorks, FaqSubBlock, FaqBlock)

admin.site.register(Question)
admin.site.register(Shop)
admin.site.register(Country)
admin.site.register(News)
admin.site.register(Category)
admin.site.register(AboutUsInformation)
admin.site.register(ImagesAboutUs)
admin.site.register(HowItWorks)
admin.site.register(ImagesHowItWorks)
admin.site.register(FaqBlock)
admin.site.register(FaqSubBlock)


