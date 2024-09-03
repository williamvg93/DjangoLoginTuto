from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from users.forms import NewUserForm

# Create your views here.
def signUp(request):

    if request.method == "POST":
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:    
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save();
                login(request, user)
                return redirect("tasks")
            except Exception as e:
                return HttpResponse(f"Error: {e}")
        else:
            return HttpResponse(f"Passwords do not match !!!")
    form = NewUserForm()
    return render(
        request,
        "layouts/user/signup.html",
        {"pageTitle": "SignUp", "mainPageTitle": "SignUp", "form": form},
    )
