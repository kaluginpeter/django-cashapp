from django.db import models


PAYMENT_TYPE_IN = 'in'
PAYMENT_TYPE_OUT = 'out'


class Payment(models.Model):
    amount = models.FloatField()
    type = models.CharField(max_length=3, choices=(
        (PAYMENT_TYPE_IN, 'Поступление'),
        (PAYMENT_TYPE_OUT, 'Расход')
    ))
    description = models.TextField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
