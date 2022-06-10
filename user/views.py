from django.shortcuts import render
from user.models import User,Contact
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import SmsSerializes,SmsModel
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def showIndex(request):
    return render(request, 'index.html')


def user_signup(request):
    return render(request, 'usersign.html')


def user_login(request):
    return render(request, 'user_login.html')


def user_registration(request):
    mobile = request.POST.get("mobile")
    email = request.POST.get("email")
    password = request.POST.get("password")
    c_password = request.POST.get("confirmpassword")
    if password == c_password:
        try:
            User(mobile=mobile, email=email, password=password).save()
            return render(request,"user_login.html")
        except IntegrityError:
            return render(request,"usersign.html",{"error":"User Already Registerd !!!"})
    else:
        return render(request, "usersign.html",{"error": "Invalid Confirm Password !!!"})


def user_login_check(request):
    mobile = request.POST.get("mobile")
    password = request.POST.get("password")
    if request.method == "POST":
        try:
            res = User.objects.get(mobile=mobile, password=password)
            request.session["user_id"] = res.idno
            return render(request,"user_profile.html",{"data":res})
        except User.DoesNotExist:
            return render(request, "user_login.html", {"error": "Invalid User !!!"})
    else:
        del request.session["user_id"]
        return user_login(request)


def user_profile(request):
    return render(request,"user_profile.html",{"data":User.objects.get(idno=request.session["user_id"])})

def update_profile(request):
    return render(request,'update_profile.html',{"data":User.objects.get(idno=request.session["user_id"])})

def update_data(request):
    mobile = request.POST.get("mobile")
    email = request.POST.get("email")
    image = request.FILES["image"]
    res = User.objects.get(idno=request.session["user_id"])
    res.mobile = mobile
    res.email = email
    res.image = image
    res.save()
    return user_profile(request)

def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request,'contactus.html')


@method_decorator(csrf_exempt,name="dispatch")
def checkmobile(request):
    mob = request.POST.get('cname')
    try:
        User.objects.get(mobile=mob)
        res = {"error": "Mobile Number Allready Registerd"}
    except User.DoesNotExist:
        res = {"message": "Mobile No is Available"}
    return JsonResponse(res)

@method_decorator(csrf_exempt,name="dispatch")
def checkemail(request):
    email = request.POST.get('cname')
    try:
        User.objects.get(email=email)
        res = {"error": "Email-Id is Allready Registerd"}
    except User.DoesNotExist:
        res = {"message": "Email-Id is Available"}
    return JsonResponse(res)



class InsertSms(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        ps = SmsSerializes(data=request.data)
        if ps.is_valid():
            # ps.save()
            print(request.data)
            message = {"message": "Inbound sms ok"}
            return Response(message)
        else:
            message = {"error": ps.errors}
            return Response(message)