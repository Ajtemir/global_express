from django.urls import path

from parcels import views


urlpatterns = [
    path('parcels/', views.ParcelListView.as_view(), name='parcels')
]
