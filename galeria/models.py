from django.db import models

# Create your models here.
class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    


    def __str__(self):
        return self.name 
    

class Arte(models.Model):
    id = models.AutoField(primary_key=True)
    art = models.ImageField(upload_to='galeria/', blank = True, null= True)
    nome_artista = models.ForeignKey(
        Artista, on_delete=models.PROTECT, related_name= 'nome_artista')
    name = models.CharField(max_length=100, blank = True, null= True) 

    def __str__(self):
        return self.name 
    