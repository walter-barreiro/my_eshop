from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import UserAccount
from django.contrib import messages


@login_required(login_url='login')
def user_account(request):
    users = Customer.objects.filter(user=request.user).first()
    initial = {
        'name': users.name,
        'birthday': users.birthday.date,
        'lastname': users.lastname,
        'phone': users.phone,
        'address': users.address,
        'country': users.country,
        'city': users.city,
        'email': users.email
    }
    if request.method == "POST":
        form = UserAccount(request.POST)
        if form.is_valid():
            # Para guardar los datos del usuario en el modelo Customer
            users = Customer.objects.filter(user=request.user).update(
                name=form.cleaned_data['name'],
                lastname=form.cleaned_data['lastname'],
                birthday=form.cleaned_data['birthday'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                country=form.cleaned_data['country'],
                city=form.cleaned_data['city'],
                email=request.user.email
            )
            # -----------------------------------------------------------
            messages.success(request, "Saved ")
    else:
        form = UserAccount(initial=initial)
    return render(request, "user_account/user_account.html", {"form": form})
