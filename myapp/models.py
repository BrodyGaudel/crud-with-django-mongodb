from django.db import models


# Create your models here.
# myapp/models.py


# myapp/models.py


class Produit(models.Model):
    #id = models.AutoField(primary_key=True)
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_de_preemption = models.DateField()

    class Meta:
        db_table = 'produit'  # Spécifiez le nom de la collection MongoDB
