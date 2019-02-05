from django.urls import include, path
from payment import views

urlpatterns = [
    path('checkout/<pk>', views.checkout_view, name='payment_checkout'),
]
