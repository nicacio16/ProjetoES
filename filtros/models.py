from django.db import models
from testes.models import Upload

# Create your models here.


class Script(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.TextField(max_length=255, verbose_name="Código", help_text="Explicar como usar o código")

    def __str__(self):
        return "{}".format(self.nome)

    

class Teste(models.Model):
    imagem = models.ForeignKey(Upload, on_delete=models.CASCADE)
    filtro = models.ForeignKey(Script, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.filtro.nome, self.imagem.description)