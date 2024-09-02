from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )  # Define los campos que deseas incluir

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "User Name"
        self.fields["username"].help_text = "Only letters and numbers"
        self.fields["email"].label = "Email"
        self.fields["email"].help_text = "Enter valid email address"
        self.fields["password1"].label = "Password"
        self.fields["password1"].help_text = "minimum 8 characters"
        self.fields["password2"].label = "Repeat Password"
        self.fields["password2"].help_text = ""
        del self.fields["usable_password"]
