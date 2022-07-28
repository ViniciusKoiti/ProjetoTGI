from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import AlunoForm
from django.urls import reverse_lazy
# Create your views here.

class AlunoCreate(CreateView):
	template_name = "usuarios/form.html"
	form_class = AlunoForm
	success_url = reverse_lazy('login')
	
