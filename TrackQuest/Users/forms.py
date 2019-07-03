from django import forms

Username_regex_field = forms.RegexField (
        label = "Username",
        max_length = 30,
        regex = r'^[0-9a-zA-Z\_\w]*$',
        help_text = "Only alphanumeric characters are allowed in the username.",
        error_messages={'invalid': ("This value must contain only letters,numbers and underscores.")}
        )

class ChangeUserNameForm(forms.Form):
    UserName = Username_regex_field


class LogIn_Form(forms.Form):
    UserName = Username_regex_field
    Password = forms.CharField(widget=forms.PasswordInput())
