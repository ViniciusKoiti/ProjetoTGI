from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Aluno

class AlunoForm(forms.ModelForm):
	email = forms.EmailField(
		label="E-mail",
		max_length=180,
		widget=forms.TextInput(attrs={'placeholder': 'E-mail'})
		)
	cpf = forms.CharField(
		label="CPF",
		max_length=14,
		widget=forms.TextInput(attrs={'placeholder': '000.000.00-00'})
		)
	password = forms.CharField(
		min_length=8,
		label = 'Senha',
		widget=forms.PasswordInput(attrs={'placeholder':'********'})
	 )
	
	class Meta: 
		model = Aluno
		fields = ['email','password','cpf','ra']
		
		
	
		
	def clean_email(self):
		e = self.cleaned_data['email']
		if Aluno.objects.filter(email=e).exists():
			raise ValidationError("O email {} já está em uso.".format(e))
			
		return e
	"""
	def clean_cpf(self):
		c = self.cleaned_data['cpf']
		if Aluno.objects.filter(cpf=c).exists():
			raise ValidationError("O cpf {} já está em uso.".format(c))
	
	def clean_cpf(self):
		c = self.cleaned_data['cpf']
		if User.objects.filter(cpf=c).exists():
			raise ValidationError("O CPF {} já está em uso.".format(c))
			
		return c
	
	def cpf_validation(self):
		c = self.clean_data['cpf']
	
	@staticmethod
	def only_number(self):
		c = self.clean_data['cpf']
		return sub('[^0-9]','',c)
"""
