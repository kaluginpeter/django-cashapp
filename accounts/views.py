from django.shortcuts import render, redirect
from accounts.forms import UserForm


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

            return redirect('/')
    else:
        form = UserForm()
    return render(
        request, 'registration/registration.html', {'form': form})
