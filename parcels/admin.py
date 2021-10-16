from django.contrib import admin

from parcels.models import Parcel


class ParcelAdmin(admin.ModelAdmin):
    exclude = ('number',)


admin.site.register(Parcel, ParcelAdmin)
