from django.urls import path
from django.urls.resolvers import URLPattern
from django.urls import path
from .views import IndexView, PerfilProfessorView, CadastroView

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('perfilprofessor/', PerfilProfessorView.as_view(), name='perfilprofessor'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
]
