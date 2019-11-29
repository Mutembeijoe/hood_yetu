from django.shortcuts import render
from django.views.generic import DetailView
from .models import Neighbourhood

# Create your views here.


class NeighbourhoodDetailView(DetailView):
    model = Neighbourhood
    template_name = 'neighbourhood.html'