from django.db import models

# Create your models here.
class Persona(models.Model):
    run = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=50)
    ape_paterno = models.CharField(max_length=50)
    ape_materno = models.CharField(max_length=50)
    imagen = models.CharField(max_length=150)
    #created_at = models.DateTimeField('date published')
    #updated_at = models.DateTimeField('date published')
    class Meta:
        db_table = 'croe_persona'    

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Region3(models.Model):
    idcom =models.AutoField(primary_key=True)
    nombre = models.DateTimeField('Nombre Region')
    class Meta:
        db_table = 'aaaaa'



class Region2(models.Model):
    idcom =models.AutoField(primary_key=True)
    nombre =  models.CharField(max_length=200)
    class Meta:
        db_table = 'harrixxx'

class Region1(models.Model):
    idcom =models.AutoField(primary_key=True)
    nombre = models.DateTimeField('Nombre Region')
    class Meta:
        db_table = 'harrisito'

class Region(models.Model):
    idcom =models.AutoField(primary_key=True)
    nombre = models.DateTimeField('Nombre Region')
    class Meta:
        db_table = 'region'

class Provincia(models.Model):
    idprov =models.AutoField(primary_key=True)
    nombre = models.DateTimeField('Nombre Provincia')
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE)
    class Meta:
        db_table = 'provincia'

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=200)
    stImagen = models.CharField(max_length=200)
    #created_at = models.DateTimeField('date published')
    #updated_at = models.DateTimeField('date published')
    class Meta:
        db_table = 'comuna'    

class Tabla_test(models.Model):
    columna_uno = models.CharField(max_length=200)
    columna_dos = models.CharField(max_length=200)
    columna_tres = models.CharField(max_length=200)
    columna_cuatro = models.CharField(max_length=200)   

class Tabla_test1(models.Model):
    columna_uno = models.CharField(max_length=200)
    columna_dos = models.CharField(max_length=200)
    columna_tres = models.CharField(max_length=200)
    columna_cuatro = models.CharField(max_length=200)   