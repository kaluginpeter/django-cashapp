from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, F, Case, When, FloatField

PAYMENT_TYPE_IN = 'in'
PAYMENT_TYPE_OUT = 'out'


class Payment(models.Model):
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE, null=True)
    amount = models.FloatField()
    type = models.CharField(max_length=3, choices=(
        (PAYMENT_TYPE_IN, 'Поступление'),
        (PAYMENT_TYPE_OUT, 'Расход')
    ))
    description = models.TextField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    @staticmethod
    def balance(user):
        balance = Payment.objects.filter(user=user).aggregate(balance=Sum(Case(
            When(type=PAYMENT_TYPE_IN, then=F('amount')),
            When(type=PAYMENT_TYPE_OUT, then=-F('amount')), output_field=FloatField())))
        return balance['balance'] or 0
