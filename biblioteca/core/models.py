<<<<<<< HEAD
from django.db import models

class LivroModel(models.Model):
    titulo = models.CharField('Título', max_length=200)
    editora = models.CharField('editora', max_length=200)
    autor = models.CharField('autor', max_length=200)

    def __str__(self):
=======
from django.db import models

class LivroModel(models.Model):
    titulo = models.CharField('Título', max_length=200)
    editora = models.CharField('editora', max_length=200)

    def __str__(self):
>>>>>>> 89d95d6168a52ef6ca3eed0cc40ea59491c33c66
        return self.titulo