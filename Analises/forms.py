from django import forms
from .models import *

class AmostraForm(forms.ModelForm):
	
	class Meta:
		model = Amostra
		fields = ['etapa_boca']
		exclude = ['nome','ph_fk','horario_fim','temperatura_fk']
		
class TemperaturaForm(forms.ModelForm):
	
	class Meta:
		model = Temperatura
		fields = ['temperatura']
		exclude = ['horario_dia']
		
class PhForm(forms.ModelForm):
	
	class Meta:
		model = Ph
		fields = ['ph']
		exclude = ['horario_dia']
		
class NomeAmostraForm(forms.ModelForm):
	
	class Meta:
		model = NomeAmostra
		fields = ["nome_amostra"]
