from django.urls import path
from users import views

urlpatterns = [
    path('sign/', views.SignView.as_view(), name='sign'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]
