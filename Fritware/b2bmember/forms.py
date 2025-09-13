from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email'] #es se form me custom fields import kr sakte h user model se (password coming from usercreationform)
        labels = {'email':'Email'} #es se page ke lable change ho jayte h


