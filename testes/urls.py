from django.urls import path
from .views import UploadCreate

urlpatterns = [
    #Exemplo: path('', IndexView.as_view(), name='inicio'),
    path('testes/upload/', UploadCreate.as_view(), name="upload-imagem"),
    path('testes/', UploadCreate.as_view(), name="imagem"),
]
