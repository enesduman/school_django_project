from django.db import models


class Sinif(models.Model):
    adi = models.TextField(verbose_name="Sınıf Adı")
    
    def __str__(self):
        return self.adi
    
