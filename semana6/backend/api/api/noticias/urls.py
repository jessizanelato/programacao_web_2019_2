from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/artigos/', views.ArtigoList.as_view()),
    path('api/artigos/<int:pk>/', views.ArtigoDetail.as_view()),
    path('api/fontes/', views.FonteList.as_view()),
    path('api/fontes/<int:pk>/', views.FonteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)