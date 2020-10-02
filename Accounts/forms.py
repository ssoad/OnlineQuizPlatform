from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from django.forms import ModelForm
from .models import Profile

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                Tuser = User.objects.filter(username=username)
                if not Tuser:
                    raise forms.ValidationError('This user does not exist')
                if not Tuser[0].check_password(password):
                    raise forms.ValidationError('Incorrect password')
                if not Tuser[0].is_active:
                    raise forms.ValidationError('This user is not active. Please your verification process')
        return super(UserLoginForm, self).clean()


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    organization = forms.CharField(label='Organization')
    email = forms.EmailField(label='Email address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=(('1', 'Examinee'), ('2', 'Examiner')))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'email2',
            'password',
        ]

    def clean(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean()


class CreateProfileForm(forms.ModelForm):
    # pro_pic = forms.ImageField(label='Profile Picture',)
    # contact_number = forms.CharField(label='Contact No')

    class Meta:
        model = Profile
        fields = ['pro_pic', 'contact_number']
