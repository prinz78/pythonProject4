from django.forms import forms
from django.contrib.auth.forms import forms, UserCreationForm, UserChangeForm
from .models import CustomUser

# Create you forms here

class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email', 'age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','age',)


