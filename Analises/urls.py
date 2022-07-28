from django.urls import path
from .views import AnaliseCreate
"""path('cadastrar',AnaliseView.as_view(),name='central'),"""

urlpatterns = [

	path('central/',AnaliseCreate.as_view(),name="central"),
]
