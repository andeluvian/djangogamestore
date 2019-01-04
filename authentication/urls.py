from django.urls import include, path
from authentication import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
