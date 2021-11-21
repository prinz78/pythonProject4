from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy
from .forms import CustomUserCreateForm
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
