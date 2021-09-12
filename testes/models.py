from django.db import models

# Create your models here.

class Upload(models.Model):
    arquivo = models.ImageField(upload_to='uploads', max_length=100)

    def __str__(self):
        return self.arquivo
