from django.urls import path

from .views import ScriptCreate

urlpatterns = [
    # Exemplo: path('', IndexView.as_view(), name='inicio'),
    path('filtros/script/', ScriptCreate.as_view(), name="cadastrar-script"),
]
