from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/index.html'

class UploadView(TemplateView):
    template_name = 'paginas/upload.html'

class ScriptView(TemplateView):
    template_name = 'paginas/script.html'

class TesteView(TemplateView):
    template_name = 'paginas/teste.html'