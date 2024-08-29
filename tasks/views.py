from django.shortcuts import render

# Create your views here.
def mainPage(request):

    return render(request, "layouts/tasks/signup.html", {"pageTitle" : "SignUp", "mainPageTitle" : "SignUp"})
