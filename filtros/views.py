from typing import ClassVar
from django.db import models
from django.views.generic import TemplateView

from .models import Script

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


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

