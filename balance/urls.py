from django.urls import path
from balance import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('create/', views.payment_create),
    path('delete/<int:payment_id>/', views.payment_delete),
    path('list/', views.payments_list, name='payments_list'),
]
