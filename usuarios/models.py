from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class Pessoa(AbstractUser,AbstractBaseUser):
    """username = models.CharField(
        verbose_name = 'Usuario',
        max_length = 255,
        unique = True,
        default = 'test'
    )
    """
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=255,
        unique=True,
        default = 'test'
    )
    cpf = models.CharField(
        max_length=14, 
        verbose_name = "CPF"
        )
   
    
    def __str__(self):
        return self.email
    
class Aluno(Pessoa):
    ra = models.CharField(
        max_length=150, 
        verbose_name = "RA"
        )

    def __str__(self):
        return "{}-({}): {}".format(self.email,self.ra)

class Professor(Pessoa):
    siape = models.CharField(
        max_length=7, 
        verbose_name = "SIAPE"
        )
    
    def __str__(self):
        return "{}-({}): {}".format(self.email,self.siape)

