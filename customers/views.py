from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserregistrationForm,CartForm,OrderForm
from administrator.models import Mobile
from .models import *
from django.db.models import Sum
# Create your views here.
# Create your views here.
def user_home(request):
    return render(request,"customers/base.html")

def user_list_all_mobiles(request):
        mobiles=Mobile.objects.all()
        context={}
        context["mobiles"]=mobiles
        return render(request,"customers/list.html",context)

def user_login(request):
    if request.method== "POST":
        username=request.POST.get("username")
        password = request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("userhome")
        else:
            pass
    return render(request,"customers/login.html")
def user_logout(request):
    logout(request)
    return redirect("userlist")

def user_mobile_details(request,id):
        mobile=Mobile.objects.get(id=id)
        context={}
        context["mobile"] =mobile
        return render(request,"customers/view.html",context)

def user_registration(request):
    form=UserregistrationForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = UserregistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            context["form"] = form
            return render(request, "customers/userregistration.html", context)

    return render(request, "customers/userregistration.html", context)


def add_to_cart(request,id):
    if request.user.is_authenticated:
        product=get_mobile_object(id)
        form=CartForm(initial={'user':request.user,'product':product})
        context={}
        context['form']=form
        if request.method=='POST':
            form=CartForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mycart')
            else:
                context['form']=form
                return render(request,'customers/view.html',context)
        return render(request, 'customers/cartitems.html', context)
    else:
        return redirect('userlogin')

# to view my cart
def view_mycart(request):
    if request.user.is_authenticated:
        carts=Cart.objects.filter(user=request.user)
        #context= {}
        #context['carts']=carts
        total=Cart.objects.filter(user=request.user).aggregate(Sum('price_total'))
        return render(request,'customers/cartview.html', {'carts':carts,'total':total})
    else:
        return redirect('userlogout')

#to remove from cart
def remove_cart_item(request,id):
    if request.user.is_authenticated:
        carts = Cart.objects.get(id=id)
        carts.delete()
        return redirect('mycart')
    else:
        return redirect('userlogout')

# function to get id of each mobile
def get_mobile_object(id):
    return Mobile.objects.get(id=id)

#to buy from cart
def cart_order(request,id):
    if request.user.is_authenticated:
        carts=Cart.objects.get(id=id)
        form=OrderForm(initial={'user':request.user,'product':carts.product})
        context={}
        context['form']=form
        if request.method=='POST':
            form=OrderForm(request.POST)
            if form.is_valid():
                form.save()
                remove_cart_item(request,id)
                return redirect('myorders')
            else:
                context['form']=form
                return render(request,'customers/ordereditems.html',context)
        return render(request, 'customers/ordereditems.html', context)
    else:
        return redirect('userlogout')

def user_list_all_orders(request):
    if request.user.is_authenticated:
        order = Orders.objects.filter(user=request.user)
        context = {}
        context['order'] = order
        return render(request, 'customers/myorder.html', context)
    else:
        return redirect('userlogout')
#to cancel order
def cancel_order(request,id):
    if request.user.is_authenticated:
        order=Orders.objects.get(id=id)
        order.status='Cancelled'
        order.save()
        return redirect('myorders')
    else:
        return redirect('userlogout')




