from .models import Fonte, Artigo
from .serializers import ArtigoSerializer, FonteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ArtigoList(APIView):
    def get(self, request, format=None):
        get_data = request.query_params
        artigos = Artigo.objects.filter(categoria=get_data['categoria'])
        serializer = ArtigoSerializer(artigos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArtigoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtigoDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Artigo.objects.get(pk=pk)
        except Artigo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        artigo = self.get_object(pk)
        serializer = ArtigoSerializer(artigo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        artigo = self.get_object(pk)
        serializer = ArtigoSerializer(artigo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        artigo = self.get_object(pk)
        serializer = ArtigoSerializer(artigo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        artigo = self.get_object(pk)
        artigo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FonteList(APIView):
    def get(self, request, format=None):
        fontes = Fonte.objects.all()
        serializer = FonteSerializer(fontes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FonteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FonteDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Fonte.objects.get(pk=pk)
        except Fonte.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fonte = self.get_object(pk)
        serializer = FonteSerializer(fonte)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fonte = self.get_object(pk)
        serializer = FonteSerializer(fonte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        fonte = self.get_object(pk)
        serializer = FonteSerializer(fonte, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fonte = self.get_object(pk)
        fonte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)