from typing import ClassVar
from django.db import models
from django.views.generic import TemplateView

from django.views.generic.edit import CreateView

from .models import Script

from django.urls import reverse_lazy

class ScriptCreate(CreateView):
    model = Script
    fields = ['nome', 'codigo']
    template_name = 'filtros/script.html'
    success_url = reverse_lazy('inicio')