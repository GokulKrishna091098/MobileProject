from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import UserregistrationForm
from administrator.models import Mobile

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
