from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.core.serializers import serialize
import json

from .models import *

# check email function
import re
def check_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def user_cost(object):
    total_cost = 0
    order_list = []
    user_id = object.user.id
    for order in OrderPizza.objects.filter(user_id = user_id):
        total_cost += order.pizzachoice.price
        order_list.append(order)
    for order in OrderSub.objects.filter(user_id = user_id):
        total_cost += order.subchoice.price
        order_list.append(order)
        # total_cost += order.subextra.price
    for order in OrderPasta.objects.filter(user_id = user_id):
        total_cost += order.pastachoice.price
        order_list.append(order)
    for order in OrderSalad.objects.filter(user_id = user_id):
        total_cost += order.saladchoice.price
        order_list.append(order)
    for order in OrderDinnerPlatter.objects.filter(user_id = user_id):
        total_cost += order.dinnerplatterchoice.price
        order_list.append(order)
    return dict(order_list = order_list, total_cost = total_cost)

menu_dict = {"pizza" : OrderPizza, "sub" : OrderSub, "pasta" : OrderPasta, "salad" : OrderSalad, "dinnerplatter" : OrderDinnerPlatter, "pizzarate" : PizzaRate, "subrate" : SubRate, "pastarate" : PastaRate, "saladrate" : SaladRate, "dinnerplatterrate" : DinnerPlatterRate}

def delete_order(menutype, pk):
    request_order = menu_dict[menutype].objects.get(pk = pk)
    request_order.delete()

def add_order(menutype, pk, others, quantity, user):
    for q in range(0,int(quantity)):
        request_order = menu_dict[f"{menutype}rate"].objects.get(pk = pk)
        place_order = menu_dict[menutype](user = user, pizzachoice = request_order)
        place_order.save()
        if others:
            if menutype == "pizza":
                toppingchoice = [ToppingChoice.objects.get(pk = o) for o in others]
                place_order.toppingchoice.set(toppingchoice)
                place_order.save()

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message" : None})
    context = {
        "pizzas" : PizzaRate.objects.all()
    }
    # return HttpResponse("Project 3: TODO")
    return render(request, "orders/index.html", context)

@login_required(login_url='/login')
def order(request):
    last_orders = user_cost(request)
    context = {
    "last_orders" : last_orders,

    "pizzatype" : serialize("json",PizzaRate.pizzatype.get_queryset()),
    "pizzasize" : serialize("json",PizzaRate.pizzasize.get_queryset()),
    "toppingtype" : serialize("json",PizzaRate.toppingtype.get_queryset()),
    "toppingchoice" : serialize("json",ToppingChoice.objects.all()),
    "pizzarate" : serialize("json",PizzaRate.objects.all()),

    "subchoice" : serialize("json", SubRate.subchoice.get_queryset()),
    "subsize" : serialize("json", SubRate.subsize.get_queryset()),
    "subextrachoice" : serialize("json", SubExtraRate.objects.all()),
    "subrate" : serialize("json", SubRate.objects.all()),

    "pastarate" : serialize("json", PastaRate.objects.all()),

    "saladrate" : serialize("json", SaladRate.objects.all()),

    "dinnerplatterrate" : serialize("json", DinnerPlatterRate.objects.all()),
    "dinnerplattersize" : serialize("json", DinnerPlatterRate.dinnerplattersize.get_queryset()),
    "dinnerplatterchoice" : serialize("json", DinnerPlatterRate.dinnerplatterchoice.get_queryset())
    }
    return render(request, "orders/order.html", context)

@login_required(login_url="/login")
def change_order(request):
    if request.method == "GET":
        return HttpResponse("Error")
    user = request.user
    menutype = request.POST['menutype']
    pk = request.POST['pk']
    todo = request.POST['todo']
    if todo == "delete":
        delete_order(menutype, pk)
    elif todo == "add":
        quantity = request.POST['quantity']
        others = request.POST['others']
        if others == "":
            others = []
        else:
            others = others.split(",")
        add_order(menutype, pk, others, quantity, user)
    return HttpResponse(todo)


def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message" : None})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message" : "Invalid credentials"})

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", { "message" : "Logged out successfully"})

def register_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "orders/login.html", {"message" : "User already logged in"})
        else:
            return render(request, "orders/register.html", {"message" : None})
    else:
        username = request.POST["username"]
        useremail = request.POST["useremail"]
        password = request.POST["password"]
        password_retype = request.POST["password_retype"]
        userlist = [u.username for u in User.objects.all()]
        if username in userlist:
            return render(request, "orders/register.html", {"message" : "User already exist"})
        if password == password_retype and check_email(useremail):
            try:
                user = User.objects.create_user(username, useremail, password)
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            except:
                return render(request, "orders/register.html", {"message" : "Error in user registration"})
        else:
            return render(request, "orders/register.html", {"message" : "Check user credentials"})
