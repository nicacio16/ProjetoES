from django.db import models
# from testes.models import Upload

# Create your models here.


class Script(models.Model):
    help_text='''Escolha entre: Imagem, Limiarização, Morfologia ou alguma outra personalizada'''
    categoria = models.CharField(max_length=50, help_text=help_text)
    nome = models.CharField(max_length=50)
    help_text='''image_in e image_out são arrays numpy.
    atribua o valor da variavel image_out a partir de image_in.'''
    codigo = models.TextField(max_length=255, verbose_name="Código", help_text=help_text)

    def __str__(self):
        return "{} - {}".format(self.categoria, self.nome)

    

# class Teste(models.Model):
#     imagem = models.ForeignKey(Upload, on_delete=models.CASCADE)
#     filtro = models.ForeignKey(Script, on_delete=models.CASCADE)

#     def __str__(self):
#         return "{} - {}".format(self.filtro.nome, self.imagem.description)
