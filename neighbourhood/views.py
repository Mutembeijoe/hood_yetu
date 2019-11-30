from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import redirect
from .models import Neighbourhood

# Create your views here.


class NeighbourhoodDetailView(DetailView):
    model = Neighbourhood
    template_name = 'neighbourhood.html'

class NeighbourhoodListView(ListView):
    model = Neighbourhood
    template_name = 'neighbourhood_list.html'


def join_neighbourhood(request, community_id):
    if(request.user.neighbourhood == None ):
        new_hood = Neighbourhood.objects.get(id=community_id)
        request.user.neighbourhood  = new_hood
        request.user.save()
        return redirect('neighbourhood',pk=1)
    else:
        # return render(request, 'neighbourhood_list.html')
         return redirect('neighbourhood_list')