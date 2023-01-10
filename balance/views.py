from django.shortcuts import render, redirect
from balance.models import Payment, PAYMENT_TYPE_IN
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def home_page(request):
    if not request.user.is_authenticated:
        return render(request, 'balance/not_auth_index.html')
    payments = Payment.objects.filter(user=request.user)[:5]
    balance = 0
    for payment in payments:
        if payment.type == PAYMENT_TYPE_IN:
            balance += payment.amount
        else:
            balance -= payment.amount
    return render(request, 'balance/index.html', {'payments': payments, 'balance': balance})


@login_required
def payment_create(request):
    if request.method == 'POST':
        data = request.POST
        Payment.objects.create(amount=data['amount'], type=data['type'], description=data['description'],
                               user=request.user)
    return redirect('home')


@login_required
def payment_delete(request, payment_id):
    if request.method == 'POST':
        payment = Payment.objects.get(id=payment_id, user=request.user)
        payment.delete()
    return redirect('home')


@login_required
def payments_list(request):
    payments = Payment.objects.filter(user=request.user)

    # get params
    page = request.GET.get('page')
    per_page = request.GET.get('per_page', 10)

    # create paginator
    paginator = Paginator(payments, per_page)
    page_obj = paginator.get_page(page)

    return render(request, 'balance/list.html', {'page_obj': page_obj})


def faq(request):
    return render(request, 'balance/faq.html')
