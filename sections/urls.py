from django.urls import path

from sections import views

urlpatterns = [
    path("FAQ/", views.FaqView.as_view(), name='FAQ'),
    path('about-us/', views.AboutUsView.as_view(), name='about-us'),
    path('how-works/', views.HowWorksView.as_view(), name='how-works'),
    path('news/', views.NewsListView.as_view(), name='news'),
    path('shop/', views.ShopListView.as_view(), name='shop'),
    path('detail-news/<slug:slug>/', views.DetailNewsView.as_view(), name='detail-news'),
    path('', views.BaseView.as_view(), name='base'),

]
