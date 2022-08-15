from django.urls import path
from .views import AnaliseCreate,conecao_temperatura

"""path('cadastrar',AnaliseView.as_view(),name='central'),"""

urlpatterns = [

	path('central/',AnaliseCreate.as_view(),name="central"),
	path('conecao_temperatura', conecao_temperatura ,name='temperatura'),
	
]
