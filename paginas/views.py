from typing import ClassVar
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'paginas/index.html'

class PerfilProfessorView(TemplateView):
    template_name = 'paginas/perfilprofessor.html'

class CadastroView(TemplateView):
    template_name = 'paginas/cadastro.html'