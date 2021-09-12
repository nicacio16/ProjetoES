from ProjetoES.paginas.views import UploadView
from django.urls import path

from .views import UploadCreate

urlpatterns = [
    #Exemplo: path('', IndexView.as_view(), name='inicio'),
    path('testes/upload/', UploadView.as_view(), name="upload-imagem")
]
