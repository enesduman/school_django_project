from django.db import models

# Create your models here.

class Okul(models.Model):
    adi = models.TextField(verbose_name="Okul Adı")
    il = models.TextField(verbose_name="Bulunduğu İl")
    
    def __str__(self):
        return self.adi
    