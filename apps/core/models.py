from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Manuais(models.Model):
    nome_manual = models.CharField(max_length=255)
    texto_manual = RichTextField()

    class Meta:
        verbose_name_plural = 'Manuais'

    def __str__(self):
        return "{}".format(self.nome_manual)
