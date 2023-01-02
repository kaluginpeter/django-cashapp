from django.shortcuts import render
from balance.models import Payment, PAYMENT_TYPE_IN
# Create your views here.
def payments_list(request):
    if request.method == 'POST':
        data = request.POST
        Payment.objects.create(amount=data['amount'], type=data['type'])
    payments = Payment.objects.all()
    balance = 0
    for payment in payments:
        if payment.type == PAYMENT_TYPE_IN:
            balance += payment.amount
        else:
            balance -= payment.amount
    return render(request, 'balance/list.html', {'payments':payments, 'balance': balance})