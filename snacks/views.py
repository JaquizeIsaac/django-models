from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    
class SnackListView(ListView):
    template_name = 'snacks/snacks_list.html'
    model = Snack
    context_object_name = 'snacks'
    
class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snacks/snacks_detail.html'
    context_object_name = 'snack'