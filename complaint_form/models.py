from django.db import models

# Create your models here.

class Categories(models.Model):
   fio = models.CharField(max_length=50, unique=True , verbose_name='ФИО')
   age = models.PositiveIntegerField()
   directions = models.CharField(max_length=50 , verbose_name='Направления')
   sex = models.CharField(max_length=50 , verbose_name='Пол')
   bthd = models.DateTimeField(verbose_name='Дата рождения')
   date_out = models.DateField(auto_now_add=True)
   file = models.FileField(upload_to='media' , verbose_name='Файл' , null=True, blank=True)

   def __str__(self) -> str:
      return self.fio
   


   
