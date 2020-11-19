from django.contrib import admin
from .models import Fonte, Artigo

class FonteAdmin(admin.ModelAdmin):
    list_display = ("nome",)

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "resumo", "conteudo", "autor", "data_publicacao", "fonte",)

admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Fonte, FonteAdmin)
