from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,ListView,DeleteView
from django.urls import reverse_lazy
from .models import Aluno,Professor
# Create your views here.

class AlunoCreate(CreateView):
    model = Aluno
    fields = ['usuario','senha','cpf','email','ra']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

class ProfessorCreate(CreateView):
    model = Professor
    fields = ['usuario','senha','cpf','email','siape']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')
'''
def AlunoUpdate(UpdateView):
    model = Aluno
    fields = ['usuario','senha','cpf','email','ra']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

def ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['usuario','senha','cpf','email','siape']
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

def AlunoDelete(DeleteView):
    model = Aluno
    template_name = 'formulario.html'
    success_url = reverse_lazy('index')

def ProfessorDelete(DeleteView):
    model = Professor
    template_name = 'formulario.html'
    success_url = reverse_lazy(index)

def AlunoList(ListView):
    model = Aluno
    template_name =
'''
