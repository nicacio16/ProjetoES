from django.urls import path

from .views import ScriptCreate

urlpatterns = [
    # Exemplo: path('', IndexView.as_view(), name='inicio'),
    path('', ScriptCreate.as_view(), name="cadastrar-script"),
]
