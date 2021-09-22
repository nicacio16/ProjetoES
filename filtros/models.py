from django.db import models

# Create your models here.


class Script(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.TextField(max_length=255, verbose_name="Código")

    def __str__(self):
        return "{} ({})".format(self.nome, self.codigo)

    