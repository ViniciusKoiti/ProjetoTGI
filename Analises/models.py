from django.db import models
from usuarios.models import Pessoa
from django.utils import timezone

#horario_fim = models.DateTimeField(default= dt.datetime.now() + dt.timedelta(hours=6)), default= dt.datetime.now() + dt.timedelta(hours=6)),

def seis_horas_depois():
	if Amostra.etapa_boca == True:
		return timezone.now() + timezone.timedelta(hours=6,minutes = 10)
	else:
		return timezone.now() + timezone.timedelta(hours=6)
		
class Ph(models.Model):
	horario_dia = models.DateTimeField(auto_now=True)
	ph = models.FloatField()

class Temperatura(models.Model):
	horario_dia = models.DateTimeField(auto_now=True)
	temperatura = models.FloatField()

class NomeAmostra(models.Model): 
	nome_amostra = models.CharField(max_length=50)

class Amostra(models.Model):
	nome = models.ForeignKey(NomeAmostra,on_delete=models.CASCADE)
	temperatura_fk = models.ForeignKey(Temperatura,on_delete=models.CASCADE)
	ph_fk = models.ForeignKey(Ph,on_delete=models.CASCADE)
	usuario_fk = models.OneToOneField(Pessoa,on_delete=models.CASCADE)
	etapa_boca = models.BooleanField(default=1)
	horario_fim = models.DateTimeField(default = seis_horas_depois)
