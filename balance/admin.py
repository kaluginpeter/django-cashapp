from django.contrib import admin
from balance.models import Payment
# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass