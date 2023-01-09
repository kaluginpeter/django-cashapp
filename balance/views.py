from django.shortcuts import render, redirect
from balance.models import Payment, PAYMENT_TYPE_IN
from django.contrib.auth.decorators import login_required


def payments_list(request):
    if not request.user.is_authenticated:
        return render(request, 'balance/index.html')
    payments = Payment.objects.filter(user=request.user)
    balance = 0
    for payment in payments:
        if payment.type == PAYMENT_TYPE_IN:
            balance += payment.amount
        else:
            balance -= payment.amount
    return render(request, 'balance/list.html', {'payments': payments, 'balance': balance})


@login_required
def payment_create(request):
    if request.method == 'POST':
        data = request.POST
        Payment.objects.create(amount=data['amount'], type=data['type'], description=data['description'],
                               user=request.user)
    return redirect('payments_list')


@login_required
def payment_delete(request, payment_id):
    if request.method == 'POST':
        payment = Payment.objects.get(id=payment_id, user=request.user)
        payment.delete()
    return redirect('payments_list')
