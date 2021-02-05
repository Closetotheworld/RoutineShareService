from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView


class ProjectListView(ListView):
    pass

class ProjectCreateView(CreateView):

    pass

class ProjectDetailView(DetailView):
    pass