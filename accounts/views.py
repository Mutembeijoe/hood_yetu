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



class UserDetailView(DetailView):
    model = CustomUser
    template_name='profile.html'

class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'edit_profile.html'
    fields = ('username', 'email', 'avatar', 'bio')
    # success_url = reverse_lazy('profile', args=[self.object.id])