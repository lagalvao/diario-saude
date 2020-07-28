from django.contrib import admin
from .models import Remedio, GrupoFarmaco, Classificacao, Intensidade, Historico, Controle, Farmaco, Analise, GrupoFarmacoII

# Registrar as tabelas no admin do django
admin.site.register(Remedio)
admin.site.register(GrupoFarmaco)
admin.site.register(Classificacao)
admin.site.register(Intensidade)
admin.site.register(Historico)
admin.site.register(Controle)
admin.site.register(Farmaco)
admin.site.register(Analise)
admin.site.register(GrupoFarmacoII)