from django.urls import path

from .views import AlunoCreate,ProfessorCreate

urlpatterns = [
	path('cadastro/aluno/', AlunoCreate.as_view(), name='cadastrar-aluno'),
	path('cadastro/professor/', ProfessorCreate.as_view(), name='cadastrar-professor'),
]
