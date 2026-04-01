from django.contrib import admin
from core.models import Dados_orcamento


class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente','data_inicial_orcamento')


admin.site.register(Dados_orcamento, EventoAdmin)