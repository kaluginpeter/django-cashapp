from django.shortcuts import render, redirect
from balance.models import Payment, PAYMENT_TYPE_IN


def payments_list(request):

    payments = Payment.objects.all()
    balance = 0

    for payment in payments:
        if payment.type == PAYMENT_TYPE_IN:
            balance += payment.amount
        else:
            balance -= payment.amount
    return render(request, 'balance/list.html', {'payments':payments, 'balance': balance})


def payment_create(request):
    if request.method == 'POST':
        data = request.POST
        Payment.objects.create(amount=data['amount'], type=data['type'])
    return redirect('payments_list')


def payment_delete(request, payment_id):
    if request.method == 'POST':
        payment = Payment.objects.get(id=payment_id)
        payment.delete()
    return redirect('payments_list')