from django.urls import path

from .views import ScriptCreate, ScriptUpdate, TesteDetail

urlpatterns = [
    # Exemplo: path('', IndexView.as_view(), name='inicio'),
    path('filtros/script', ScriptCreate.as_view(), name="cadastrar-script"),
    path('filtros/editar/script/<int:pk>', ScriptUpdate.as_view(), name="editar-script"),

    path('teste/<int:pk>', TesteDetail.as_view(), name="ver-teste"),
]
