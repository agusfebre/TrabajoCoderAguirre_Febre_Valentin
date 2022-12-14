from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    precio=models.FloatField()
    
    def __str__(self) -> str:
        return str(self.codigo)+" "+self.nombre+" "+self.marca

class Proveedor(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()

    def __str__(self) -> str:
        return self.nombre

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self) -> str:
        return self.nombre+" "+self.apellido+" "+self.email