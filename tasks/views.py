from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from tasks.forms import NewUserForm

# Create your views here.
def mainPage(request):

    form = NewUserForm()
    #if "id_usable_password" in form.fields:
     #   del form.fields["id_usable_password"]

    return render(
        request,
        "layouts/tasks/signup.html",
        {"pageTitle": "SignUp", "mainPageTitle": "SignUp", "form": form},
    )
