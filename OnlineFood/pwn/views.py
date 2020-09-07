from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,StateModel
from pwn.forms import Stateform
from django.contrib import messages

def showIndex(request):
    return render(request,"pwn/login.html")


def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),
                                                password=request.POST.get("pwn_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "pwn/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "pwn/login.html", {"error": "Admin Logout Success"})



def welcome(request):
    return render(request,"pwn/home.html")


def openState(request):
    state_data = StateModel.objects.all()
    return render(request, "pwn/openstate.html", {"form": Stateform,"X":state_data})

def save_state(request):
    sf = Stateform(request.POST)
    state_data = StateModel.objects.all()
    if sf.is_valid():
        sf.save()
        messages.success(request, "Registered Successfully")
        return render(request, "pwn/openstate.html", {"form":Stateform, "X": state_data})
    elif request.GET:
        g=request.GET.get("name")
        up1=request.POST.get("u1")
        up2=request.POST.get("u2")
        StateModel.objects.filter(name=g).update(name=up1,photo=up2)
        messages.success(request, "Updated Successfully")
        return render(request, "pwn/openstate.html", {})
    else:
        return render(request, "pwn/openstate.html", {"form":Stateform, "X": state_data})

def deletestate(request):
    x=request.GET.get("no")
    StateModel.objects.filter(name=x).delete()
    y=StateModel.objects.all()
    return render(request,"pwn/openstate.html",{"X":y,"form":Stateform})
#def updateschedule(request):
#    x=request.GET.get("no")
def updatestate(request):
    y = StateModel.objects.all()
    x = request.GET.get("name")
    data = StateModel.objects.get(name=x)
    return render(request,"pwn/openstate.html",{"X":y,"form":Stateform,"update":data})

def openCity(request):
    return render(request,"pwn/opencity.html")


def openCusine(request):
    return render(request,"pwn/opencuisine.html")


def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReporsts(request):
    return render(request,"pwn/openreports.html")