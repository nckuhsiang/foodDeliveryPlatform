from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.utils.translation import get_language_from_path

from Account.models import User
# Create your views here.
def getLoginPage(request):
    return render(request,"login.html")
def getRegisterPage(request):
    return render(request,"register.html")
def login(request):
    account = request.POST.get('account')
    password = request.POST.get('password')
    try:
        user = User.objects.get(account=account,password=password)
        print(user)
        return HttpResponse(True)
    except:
        return HttpResponse(False)
def register(request):
    try:
        account = request.POST.get('account')
        password = request.POST.get('password')
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        if gender == "1":
            gender = True
        else:
            gender = False
        user = User.objects.create(account=account,password=password,name=name,address=address,email=email,phone=phone,birthday=birthday,gender=gender)
        user.save()
        return HttpResponse("success")
    except Exception as e:
        return HttpResponse(e)
def checkAccountValid(request):
    account = request.GET.get('account')
    print(account)
    try:
        _ = User.objects.get(account=account)
        return HttpResponse(False)
    except:
        return HttpResponse(True)