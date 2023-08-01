from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method=='POST':
        username = request.POST['user_name']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        user = User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
        user.save();
    return render(request,'register.html')
