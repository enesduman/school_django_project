from django.db import models
from django.contrib.auth.models import AbstractUser
from okul.models import Okul
from classes.models import Sinif


class UserTypes(models.IntegerChoices):
    DIRECTOR = 1,'Müdür'
    TEACHER = 2,'Öğretmen'
    STUDENT = 3,'Öğrenci'
    
class Account(AbstractUser):
    name = models.CharField(max_length=100,verbose_name="Ad Soyad")
    user_type = models.IntegerField(verbose_name="Kullanıcı Tipi",choices=UserTypes.choices,default=UserTypes.STUDENT)
    okul = models.ForeignKey(Okul,on_delete=models.CASCADE,related_name='accounts',null=True)
    sinif = models.ForeignKey(Sinif,on_delete=models.CASCADE,related_name='accounts',null=True)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
