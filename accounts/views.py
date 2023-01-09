
from django.shortcuts import render, redirect
from accounts.forms import UserForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'registration/registration.html', {'form': form})