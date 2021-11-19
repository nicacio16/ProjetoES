from django.urls import path
from django.urls.resolvers import URLPattern
from .views import IndexView, UploadView, ScriptView, TesteView
from testes.views import showimage

urlpatterns = [
    path('', showimage, name='inicio'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('script/', ScriptView.as_view(), name='script'),
    path('teste/', TesteView.as_view(), name='teste'),    
]