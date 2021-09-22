from typing import ClassVar
from django.db import models
from django.views.generic import TemplateView

from .models import Script, Teste

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.conf import settings

import os

class ScriptCreate(CreateView):
    model = Script
    fields = ['nome', 'codigo']
    template_name = 'filtros/form.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Inserir Filtro"
        context['botao'] = "Cadastrar"

        return context


class ScriptUpdate(UpdateView):
    model = Script
    fields = ['nome', 'codigo']
    template_name = 'filtros/form.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Filtro"
        context['botao'] = "Atualizar"

        return context


class TesteDetail(DetailView):
    model = Teste
    template_name = 'filtros/teste.html'

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        # Aqui que fazer aquele EXEC e aplicar os filtros

        #pega o caminho completo do diretório atual
        dir_atual = settings.BASE_DIR
        
        # pegar a imagem
        img = self.object.imagem.image

        codigo = self.object.filtro.codigo

        # Substituir sua notação pelo real código a ser utilizado
        codigo = codigo.replace('$imagem$', img.url)
        codigo = codigo.replace('$imagem_final$', os.path.join(dir_atual, 'uploads/resultado_imagem.jpg'))


        context['resultado'] = dir_atual
        context['resultado_img'] = os.path.join(dir_atual, str(img)).replace('\\', '/')

        return context

