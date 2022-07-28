from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Amostra

"""
class AnaliseView(ListView):
	template_name = "analises/central.html"
	model = Amostra
"""	
class AnaliseCreate(CreateView):
	template_name = "analises/central.html"
	model = Amostra
	fields = '__all__'
	success_url = reverse_lazy('central')
# Create your views here.
