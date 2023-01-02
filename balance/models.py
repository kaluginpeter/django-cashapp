from django.db import models

PAYMENT_TYPE_IN = 'in'
PAYMENT_TYPE_OUT = 'out'

# Create your models here.
class Payment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    type = models.CharField(max_length=3, choices=(
        (PAYMENT_TYPE_IN, 'Поступление'),
        (PAYMENT_TYPE_OUT, 'Расход')
    ))
    class Meta:
        ordering = ('-created',)