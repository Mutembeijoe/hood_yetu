from django.urls import path
from .views import NeighbourhoodDetailView

urlpatterns = [
    path('<int:pk>/',NeighbourhoodDetailView.as_view(),name='neighbourhood')
]