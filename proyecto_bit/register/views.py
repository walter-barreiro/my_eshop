from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from user_account.models import Customer
from shopping_cart.models import Order


def register(request):
    # Para que el usuario no pueda acceder al registro si ya esta logueado
    if request.user.is_authenticated:
        return redirect('home')
    # --------------------------------------------------------------------
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                # loguear usuario luego de registrarlo ------
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=user, password=password)
                login(request, user)
                # ------------------------------------------
                # Creo un nuevo cliente
                c = Customer(user=user)
                c.save()
                # # Creo una nueva Order vacia
                order = Order(owner=c)
                order.save()
                # ---------------------
                return redirect('/')
        else:
            form = RegisterForm()
        return render(request, "register/register.html", {"form": form})


def loginPage(request):
    # Para que el usuario no pueda acceder a login si ya esta logueado
    if request.user.is_authenticated:
        return redirect('home')
    # --------------------------------------------------------------------
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Username or password is incorrect")

        return render(request, "registration/login.html", {})


def logoutUser(request):
    logout(request)
    return redirect("login")
