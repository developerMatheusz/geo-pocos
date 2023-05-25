from django.contrib.gis.db import models

class County(models.Model):
    nome = models.CharField(max_length=40)
    cod_ibge_m = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.nome
