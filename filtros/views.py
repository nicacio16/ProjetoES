from typing import ClassVar
from django.db import models
from django.views.generic import TemplateView

# from .models import Teste
from .models import Script

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.conf import settings

import os
import math
import cv2


class ScriptCreate(CreateView):
    model = Script
    fields = ['categoria', 'nome', 'codigo']
    template_name = 'filtros/form.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Inserir Filtro"
        context['botao'] = "Cadastrar"

        return context


# class TesteCreate(CreateView):
#     model = Teste
#     fields = ['imagem', 'filtro']
#     template_name = 'filtros/form.html'
#     success_url = reverse_lazy('inicio')

#     def get_context_data(self, *args, **kwargs):

#         context = super().get_context_data(*args, **kwargs)

#         context['titulo'] = "Inserir Imagem"
#         context['botao'] = "Upload"

#         return context


class ScriptUpdate(UpdateView):
    model = Script
    fields = ['categoria', 'nome', 'codigo']
    template_name = 'filtros/form.html'
    success_url = reverse_lazy('inicio')

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Filtro"
        context['botao'] = "Atualizar"

        return context


# class TesteUpdate(UpdateView):
#     model = Teste
#     fields = ['imagem', 'filtro']
#     template_name = 'filtros/form.html'
#     success_url = reverse_lazy('inicio')

#     def get_context_data(self, *args, **kwargs):

#         context = super().get_context_data(*args, **kwargs)

#         context['titulo'] = "Editar Imagem"
#         context['botao'] = "Atualizar"

#         return context


# class TesteDetail(DetailView):
#     model = Teste
#     template_name = 'filtros/teste.html'

#     def get_context_data(self, *args, **kwargs):
#         # print([i for i in TesteDetail.model.objects.filter()])
#         print([i.filtro.nome for i in TesteDetail.model.objects.filter()])
#         # print(TesteDetail.model.objects.filter(pk=2)[0].imagem.image.url)
#         context = super().get_context_data(*args, **kwargs)
#         dir_atual = settings.BASE_DIR
#         img = self.object.imagem.image
#         codigo = self.object.filtro.codigo
#         url_out=img.url+'_result.png'
#         #NÃO REMOVER $image_in. ele é usado em $loc.
#         image_in=cv2.imread('.'+img.url)
#         loc=locals()
#         print(codigo)
#         exec(codigo, globals(),loc)
#         cv2.imwrite('.'+url_out, loc['image_out'])

#         context['resultado'] = dir_atual
#         # context['resultado_img'] = os.path.join(dir_atual, str(img)).replace('\\', '/')
#         context['resultado_img'] = url_out

#         return context

