from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from random import randint


class SignupForm(UserCreationForm):
    username = None
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email'] #es se form me custom fields import kr sakte h user model se (password coming from usercreationform)
        labels = {'email':'Email'} #es se page ke lable change ho jayte h

    def generate_unique_username(self):
        while True:
            username = f"FRIT{randint(100000, 999999)}"
            if not User.objects.filter(username=username).exists():
                return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.generate_unique_username()
        if commit:
            user.save()
        return user


