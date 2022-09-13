import uuid

from django.shortcuts import render
from .models import Users


# Create your views here.
def home(request):
    return render(request, 'login.html')


def getUUID():
    return uuid.uuid1()


def sendOtp():
    pass


def texteditor(request):
    return render(request, 'textarea.html')


def login(request):
    if request.method == 'POST':
        name = request.POST['email']
        password = request.POST['password']
        print(name + " and " + password)
        try:
            user = Users.objects.get(emailId=name)
            if user.password == password:
                print("user Verified")
                return render(request, 'textarea.html')
        except Exception as e:
            print("User not found")
    return render(request, 'login.html')


def signin(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(name + " " + email + " " + password)
        users = Users()
        if name == "" or email == "" or password == "":
            return render(request, 'login.html')
        users.name = name
        users.emailId = email
        users.password = password
        try:
            users.save()
        except Exception as e:
            print("Something went wrong for saving users details")
        print("users data saved")
    return render(request, 'login.html')


def forget(request):
    return render(request, 'forgetPassword.html')
