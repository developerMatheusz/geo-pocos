from django.contrib.gis.db import models
from django.template.defaultfilters import date

class Pit(models.Model):
    proprietario = models.CharField('proprietário', max_length=254)
    orgao = models.CharField('orgão', max_length=254)
    data_perfuracao = models.DateField('data de perfuração')
    profundidade = models.FloatField('profundidade (m)')
    q_m3h = models.FloatField('q (m3/h)')
    equipamento = models.CharField('equipamento', max_length=254, null=True)
    geom = models.PointField('geom', srid=4326)

    def __str__(self):
        return self.proprietario
    
    @property
    def popup_content(self):
        popup = '<span>Proprietário: </span>{}'.format(self.proprietario)
        popup += '<span>Órgão: </span>{}'.format(self.orgao)
        popup += "<span>Data de Perfuração: </span>{}".format(date(self.data_perfuracao, "d/m/Y"))
        popup += '<span>Profundidade (m): </span>{}'.format(self.profundidade)
        popup += '<span>Vazão (m3/h): </span>{}'.format(self.q_m3h)
        popup += '<span>Equipamento: </span>{}'.format(self.equipamento)

        return popup
