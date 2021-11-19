from django.urls import path

# from .views import ScriptCreate, ScriptUpdate, TesteDetail
from .views import ScriptCreate, ScriptUpdate
urlpatterns = [
    # Exemplo: path('', IndexView.as_view(), name='inicio'),
    
    # path('testes/upload/', showimage, name="upload-imagem"),
    path('filtros/script', ScriptCreate.as_view(), name="cadastrar-script"),
    path('filtros/editar/script/<int:pk>', ScriptUpdate.as_view(), name="editar-script"),

    # path('teste/<int:pk>', TesteDetail.as_view(), name="ver-teste"),
]
