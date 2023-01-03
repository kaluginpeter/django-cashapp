from django.contrib import admin
from balance.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
