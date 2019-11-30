from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.shortcuts import redirect
from .models import Neighbourhood, Business

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


def leave_neighbourhood(request, community_id):
    if request.method == 'GET':
        return render(request, 'neighbourhood_leave.html')
    else:
        request.user.neighbourhood = None
        request.user.save()
        return redirect('mainpage')

# def search_results(request):
    # search_term = request.GET.get('search_term')
    # hood = request.GET.get('hood')
    # # print(search_results, hood)
    
    # businesses = Business.search_business(search_term,hood)
    # if businesses:
    #     return render(request,'neighbourhood.html', context={'object_list':businesses})
    # else:
    #     return render(request,'neighbourhood.html')


class CreateBusinessView(CreateView):
    model = Business
    template_name = 'business_create.html'
    fields = ('image','name','location','description','category')

    def form_valid(self, form): 
        form.instance.neighbourhood = self.request.user.neighbourhood
        return super().form_valid(form)