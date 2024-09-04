from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from users.forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

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
    else:
        form = NewUserForm()
        return render(
            request,
            "layouts/user/signUp.html",
            {"pageTitle": "SignUp", "mainPageTitle": "SignUp", "form": form},
        )


def logout_user(request):
    logout(request)
    return redirect("home")


def signIn(request):

    if request.method == 'POST':
        print(request.POST)
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(user)
        if user is None:
            return render(
                request,
                "layouts/user/signin.html",
                {
                    "pageTitle": "SignIn",
                    "mainPageTitle": "SignIn",
                    "form": AuthenticationForm,
                    "msgError" : "Invalid username or password",
                },
            )
        else:
            login(request, user)
            return redirect('home')
    else:
        return render(request, "layouts/user/signin.html", {"pageTitle": "SignIn", "mainPageTitle": "SignIn", "form" : AuthenticationForm})
