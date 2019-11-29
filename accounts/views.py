from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm
# Create your views here.


class UserRegistrationView(CreateView):
    # model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration.html'

