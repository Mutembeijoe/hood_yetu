from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
# Create your views here.


class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')



class UserDetailView(DetailView):
    model = CustomUser
    template_name='profile.html'