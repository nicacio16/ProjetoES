from typing import ClassVar
from django.db import models
from django.views.generic import TemplateView

from django.views.generic.edit import CreateView

from .models import Upload

from django.urls import reverse_lazy

class UploadCreate(CreateView):
    model = Upload
    fields = ['arquivo']
    template_name = 'testes/upload.html'
    success_url = reverse_lazy('inicio')
