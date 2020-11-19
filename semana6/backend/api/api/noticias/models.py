from django.db import models
from django.utils import timezone

class Fonte(models.Model):
    nome = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ("Fonte")
        verbose_name_plural = ("Fontes")
    
    def __str__(self):
        return self.nome

class Artigo(models.Model):
    CATEGORIAS = [
        ('geral', 'Geral'),
        ('tecnologia', 'Tecnologia'),
        ('saude', 'Saúde'),
        ('negocios', 'Negócios'),
        ('entretenimento', 'Entretenimento'),
        ('esportes', 'Esportes'),
    ]

    titulo = models.CharField(max_length=200)
    conteudo = models.TextField(blank=True)
    resumo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='geral')
    data_publicacao = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))    
    fonte = models.ForeignKey(Fonte, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Artigo")
        verbose_name_plural = ("Artigos")
    
    def __str__(self):
        return self.titulo
