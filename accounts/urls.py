from django.urls import path
from .views import UserRegistrationView, UserDetailView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile')
]