from .models import Artigo, Fonte
from rest_framework import serializers

class FonteSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Fonte
        fields = ['nome']

class ArtigoSerializer(serializers.ModelSerializer):   
    fonte = serializers.SlugRelatedField(many=False, read_only=False, queryset=Fonte.objects.all(),slug_field='nome') # permite trazer o campo do objeto e não o ID
    class Meta:
        model = Artigo
        fields = ['id', 'titulo', 'resumo', 'autor', 'categoria', 'data_publicacao', 'fonte']
