from django.shortcuts import render
from django.views.generic import CreateView
from .models import Post

# Create your views here.


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ('title', 'body', 'tags')


    def form_valid(self, form): # new
        form.instance.author = self.request.user
        form.instance.neighbourhood = self.request.user.neighbourhood
        return super().form_valid(form)
