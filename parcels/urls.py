from django.urls import path

from parcels import views

urlpatterns = [
    path('parcels', views.ParcelsView.as_view(), name='parcels'),
]