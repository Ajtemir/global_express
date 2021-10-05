from django.urls import path
from users import views

urlpatterns = [

    path('sign/', views.SignView.as_view(), name='sign'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('reset/<int:pk>/<str:token>/', views.ForgetView.as_view(), name='reset'),
    path('logout/', views.logout_view, name='logout'),
    path('personal-area/', views.PersonalAreaView.as_view(), name='personal-area'),

    # ajax
    path('forget-password/', views.ForgetPasswordView.as_view(), name='forget-password'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('change-profile/', views.ChangeProfileView.as_view(), name='change-profile'),
]
