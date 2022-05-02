from django import forms


class SignUpForm(forms.Form):
    Username = forms.CharField(max_length=20)
    Password = forms.CharField(widget=forms.PasswordInput)
    Password_Confirmation = forms.CharField(widget=forms.PasswordInput)
    Email_Address = forms.EmailField(required=True)
    Email_Confirmation = forms.EmailField(required=True)
