from django.db import models
from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
ACTION_CHOICES = (
    ('NO_FILTER', 'no filter'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert'),
)

class Upload(models.Model):
    image = models.ImageField(upload_to='uploads', verbose_name='Imagem')
    action = models.CharField(max_length=50, choices=ACTION_CHOICES, verbose_name='Ação', help_text='Aqui você coloca um texto')
    description = models.CharField(max_length=60, verbose_name='Descrição da imagem')

    def __str__(self):
        return f"[{self.pk}] {self.description}"

    # def save(self, *args, **kwargs):

    #     # open image
    #     pil_img = Image.open(self.image)

    #     # convert the image to array and do some processing
    #     cv_img = np.array(pil_img)
    #     img = get_filtered_image(cv_img, self.action)

    #     # convert back to pil image
    #     im_pil = Image.fromarray(img)

    #     # save
    #     buffer = BytesIO()
    #     im_pil.save(buffer, format='png')
    #     image_png = buffer.getvalue()

    #     self.image.save(str(self.image), ContentFile(image_png), save=False)

    #     super().save(*args, **kwargs)
