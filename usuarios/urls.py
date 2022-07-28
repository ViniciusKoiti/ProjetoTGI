
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AlunoCreate
from django.views.generic.edit import CreateView
#teste
urlpatterns = [
	#path('',view,name =""),
        path('login/',auth_views.LoginView.as_view(
            template_name="usuarios/login.html"
            ),
             name="login"),
	path('logout/',auth_views.LogoutView.as_view(),name = "logout"),
	path('cadastrar/',AlunoCreate.as_view(),name='registrar'),
]
