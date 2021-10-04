from django.urls import path

from sections import views

urlpatterns = [
    path("FAQ/", views.FaqView.as_view(), name='FAQ'),

]
