from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,StateModel,CityModel,CuisineModel
from pwn.forms import Stateform,Cityform,Cuisineform
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
        g=request.GET.get("no")
        up1=request.POST.get("u1")
        up2=request.POST.get("u2")
        StateModel.objects.filter(name=g).update(name=up1,photo=up2)
        messages.success(request, "Updated Successfully")
        return render(request, "pwn/openstate.html", {"form":Stateform, "X": state_data})
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
    x = request.GET.get("no")
    data = StateModel.objects.get(name=x)
    return render(request,"pwn/openstate.html",{"X":y,"form":Stateform,"update":data})

def openCity(request):
    city_data = CityModel.objects.all()
    return render(request, "pwn/opencity.html", {"form": Cityform,"X":city_data})

def save_city(request):
    cf = Cityform(request.POST)
    city_data = CityModel.objects.all()
    if cf.is_valid():
        cf.save()
        messages.success(request, "Registered Successfully")
        return render(request, "pwn/opencity.html", {"form":Cityform, "X": city_data})
    elif request.GET:
        g=request.GET.get("no")
        up1=request.POST.get("u1")
        up2=request.POST.get("u2")
        StateModel.objects.filter(name=g).update(name=up1,photo=up2)
        messages.success(request, "Updated Successfully")
        return render(request, "pwn/opencity.html", {"form":Cityform, "X": city_data})
    else:
        return render(request, "pwn/opencity.html", {"form":Stateform, "X": city_data})

def deletecity(request):
    x=request.GET.get("no")
    StateModel.objects.filter(name=x).delete()
    y=StateModel.objects.all()
    return render(request,"pwn/opencity.html",{"X":y,"form":Stateform})
#def updateschedule(request):
#    x=request.GET.get("no")
def updatecity(request):
    y = StateModel.objects.all()
    x = request.GET.get("no")
    data = StateModel.objects.get(name=x)
    return render(request,"pwn/opencity.html",{"X":y,"form":Stateform,"update":data})

def openCusine(request):
    cuisine_data = CuisineModel.objects.all()
    return render(request, "pwn/opencuisine.html", {"form": Cuisineform,"X":cuisine_data})

def save_cuisine(request):
    cf = Cuisineform(request.POST)
    cuisine_data = CuisineModel.objects.all()
    if cf.is_valid():
        cf.save()
        messages.success(request, "Registered Successfully")
        return render(request, "pwn/opencuisine.html", {"form":Cuisineform, "X": cuisine_data})
    elif request.GET:
        g=request.GET.get("no")
        up1=request.POST.get("u1")
        up2=request.POST.get("u2")
        CuisineModel.objects.filter(name=g).update(name=up1,photo=up2)
        messages.success(request, "Updated Successfully")
        return render(request, "pwn/opencuisine.html", {"form":Cuisineform, "X": cuisine_data})
    else:
        return render(request, "pwn/opencuisine.html", {"form":Cuisineform, "X": cuisine_data})

def deletecuisine(request):
    x=request.GET.get("no")
    CuisineModel.objects.filter(name=x).delete()
    y=CuisineModel.objects.all()
    return render(request,"pwn/opencuisine.html",{"X":y,"form":Cuisineform})
#def updateschedule(request):
#    x=request.GET.get("no")
def updatecuisine(request):
    y = CuisineModel.objects.all()
    x = request.GET.get("no")
    data = CuisineModel.objects.get(name=x)
    return render(request,"pwn/opencuisine.html",{"X":y,"form":Cuisineform,"update":data})



def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReporsts(request):
    return render(request,"pwn/openreports.html")