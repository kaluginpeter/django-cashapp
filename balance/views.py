from django.shortcuts import render

# Create your views here.
def payments_list(request):
    return render(request, 'balance/list.html')