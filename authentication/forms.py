from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('This user does not exist')
        if not user.check_password(password):
            raise forms.ValidationError('Password mismatch, please check password')
        if not user.is_active:
            raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address')
    email2 = forms.EmailField(label='Confirm email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError(
                "The user is already registered"
            )

        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails do not match")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email is already registered"
            )

        return super(UserRegistrationForm, self).clean(*args, **kwargs)
