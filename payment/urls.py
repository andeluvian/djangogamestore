from django.urls import include, path
from payment import views


urlpatterns = [
    path('checkout/<pk>', views.checkout_view, name='payment_checkout'),
    path('checkout/verification/', views.verification_view, name='payment_verification'),
    path('transactions/', views.list_view, name='payment_list'),
    path('transactions/<uuid>', views.detail_view, name='payment_detail'),
    path('sales/<pk>', views.sales_view, name='payment_sales'),
]
