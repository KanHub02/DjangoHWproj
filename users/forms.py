from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    GENDER_TYPE = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    )
    OCCUPATION_CHOICE = (
        ("Student", "Student"),
        ("Worker", "Worker"),
        ("Jobless", "Jobless"),
        ("Retired", "Retired")
    )
    FAV_CHOICE = (
        ('DRAMA', 'DRAMA'),
        ('FANTASY', 'FANTASY'),
        ('EDU', 'EDU'),
        ('ROMANTIC', 'ROMANTIC'),
        ('HORROR', 'HORROR'),
    )
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    occupation = forms.ChoiceField(choices=OCCUPATION_CHOICE, required=True)
    email = forms.EmailField(required=True)
    age = forms.DateField(required=True)
    phone_number = forms.CharField(required=True)
    favorite_genre = forms.ChoiceField(choices=FAV_CHOICE, required=False)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "gender",
            "occupation",
            "age",
            "phone_number",
            "favorite_genre"
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    email = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'please type email',
                'id': 'email',

            }
        )
    )
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "please type username",
                "id": "username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "please type password",
                "id": "password"
            }
        )
    )
