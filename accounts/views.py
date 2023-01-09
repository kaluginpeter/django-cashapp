from django.shortcuts import render, redirect
from accounts.forms import UserForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            messages.success(request, 'Аккаунт создан успешно!')
            messages.info(request, 'Пожалуйста войдите в аккаунт, чтобы продолжить.')
            return redirect('login')
    else:
        form = UserForm()
    return render(
        request, 'registration/registration.html', {'form': form})
