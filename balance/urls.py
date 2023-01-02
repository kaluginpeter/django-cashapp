from django.urls import path
from balance import views
urlpatterns = [path('', views.payments_list)]