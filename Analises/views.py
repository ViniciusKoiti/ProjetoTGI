from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Amostra,Temperatura

from django.http import HttpResponseRedirect

from .forms import AmostraForm,TemperaturaForm,PhForm,NomeAmostraForm

import serial
import time
import sqlite3


"""
class AnaliseView(ListView):
	template_name = "analises/central.html"
	model = Amostra
"""	
"""
class AnaliseCreate(CreateView):
	template_name = "analises/central.html"
	model = Amostra
	fields = ['nome','ph_fk','etapa_boca']
	model = Temperatura
	success_url = reverse_lazy('central')
"""
"""
class AnaliseCreate(CreateView):
	model = Amostra
	template_name = "analises/central.html"
	success_url = reverse_lazy('central')
	fields = ['temperatura_fk']
"""
"""
class AnaliseCreate(TemplateView):
	analise_formulario = AmostraForm()
	temperatura_formulario = TemperaturaForm()
	template_name = 'analises/central.html'
	
	def post(self,request):
		post_data = request.POST or None
		analise_form = self.analise_formulario(post_data,prefix='post')
		temperatura_form = self.temperatura_formulario(post_data,prefix='post')
		
		context = self.get_context_data(analise_form=analise_form,temperatura_form=temperatura_form)
		
		if analise_form.is_valid() and temperatura_form.is_valid():
			self.form_save(analise_form)
			self.form_save(temperatura_form)
		
		return self.render_to_response(context)  

		def form_save(self,form):
			if request.POST():
				if analise_form.is_valid() and temperatura_form.is_valid():

					a = AmostraFormulario.save()
					t = TemperaturaFormulario.save(commit=false)
					a.temperatura_fk = t.id
					t.save()
					
					messages.success(self.request, "{} saved successfully".format(obj))
			return a 
"""

class AnaliseCreate(TemplateView):
	template_name = 'analises/central.html'
	success_url = reverse_lazy('central')
	
	def get_context_data(self, **kwargs):
		kwargs['amostra'] = AmostraForm()
		kwargs['temperatura'] = TemperaturaForm()
		kwargs['PH'] = PhForm()
		return super().get_context_data(**kwargs)
		
	def form_valid(self, form):
		if request.POST():
			amostra = AmostraForm(request.POST)
			temperatura = TemperaturaForm(request.POST)
			PH = PhForm(request.POST)
		
			if amostra.is_valid() and temperatura.is_valid() and PH.is_valid():
				a = amostra.save()
				t = temperatura.save(commit=False)
				p = PH.save(commit=False)
				t.id = a.temperatura_fk
				p.id = a.ph_fk
				t.save()
				p.save()
				
		super().post(request, *args, **kwargs)	
		return redirect(self.get_redirect_url())	 
	
	
	def get_redirect_url(self):
		return self.redirect_url
		
def conecao_temperatura(request):
	while True: #Loop para a conexão com o Arduino
		try:  #Tenta se conectar, se conseguir, o loop se encerra
			arduino = serial.Serial('/dev/ttyACM0', 9600)
			print('Arduino conectado')
			break
		except:
			print('falha na conexão')
			pass
	while True:
		msg = arduino.readline().decode('utf-8').rstrip()

		print(msg)
		temperatura = (msg[13:18])
		temperatura_float = float(temperatura)
		print(temperatura)
		time.sleep(1)
		if temperatura_float > 37.00:
			salvando_temperatura = Temperatura(temperatura=temperatura_float)
			salvando_temperatura.save() 
		return HttpResponse(temperatura)
	
"""
class MultipleFormsMixin(FormMixin):
	template_name = 'central.html'
	success_url = '/central.html'
	form_classes = {AmostraForm,TemperaturaForm} # set the form classes as a mapping
	
	def get_form_classes(self):
		return self.form_classes

	def get_forms(self, form_classes):
		return dict([(key, klass(**self.get_form_kwargs())) \
			for key, klass in form_classes.items()])

	def forms_valid(self, forms):
		return super(MultipleFormsMixin, self).form_valid(forms)

	def forms_invalid(self, forms):
		return self.render_to_response(self.get_context_data(forms=forms))
"""     				
					
