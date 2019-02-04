from django.urls import include, path
from payment import views

urlpatterns = [
    path('payment/<id>', views.payment_view, name='payment'),
    path('payment/list/', views.list_view, name='payment_list'),
    path('payment/list/<uuid>', views.detail_view, name='payment_detail'),
    path('payment/processing/', views.processing_view, name='payment_processing'),
]
