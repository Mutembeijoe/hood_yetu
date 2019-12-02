from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
# Create your views here.


class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')



class UserDetailView(LoginRequiredMixin,DetailView):
    model = CustomUser
    template_name='profile.html'
    login_url = 'login'

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = CustomUser
    template_name = 'edit_profile.html'
    fields = ('username', 'email', 'avatar', 'bio')
    login_url = 'login'
    # success_url = reverse_lazy('profile', args=[self.object.id])