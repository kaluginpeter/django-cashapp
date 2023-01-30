from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from balance.models import Payment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def home_page(request):
    if not request.user.is_authenticated:
        return render(request, 'balance/not_auth_index.html')
    payments = Payment.objects.filter(user=request.user)[:5]
    return render(request, 'balance/index.html', {'payments': payments, 'balance': Payment.balance()})


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
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def payments_list(request):
    payments = Payment.objects.filter(user=request.user)

    if (sort := request.GET.getlist('sort')):
        payments = payments.order_by(*sort)

    # get params
    page = request.GET.get('page')
    per_page = request.GET.get('per_page', 10)

    # create paginator
    paginator = Paginator(payments, per_page)
    page_obj = paginator.get_page(page)

    return render(request, 'balance/list.html',
                  {'page_obj': page_obj, 'balance': Payment.balance(), 'table_headers': {
                      'amount': 'Сумма',
                      'type': 'Тип операции',
                      'description': {
                          'value': 'Описание',
                          'sort': False,
                      },
                      'created': 'Время'
                  }})


def faq(request):
    return render(request, 'balance/faq.html')
