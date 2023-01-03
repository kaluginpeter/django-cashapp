from django.urls import path
from balance import views


urlpatterns = [
    path('', views.payments_list, name='payments_list'),
    path('create/', views.payment_create)
]