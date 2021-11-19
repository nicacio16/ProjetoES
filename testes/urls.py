from django.urls import path
from .views import  showimage
# from .views import UploadCreate

urlpatterns = [
    #Exemplo: path('', IndexView.as_view(), name='inicio'),
    # path('', showimage, name="upload-imagem"),
    path('testes/upload/', showimage, name="upload-imagem"),
    # path('testes/', UploadCreate.as_view(), name="imagem"),
]
