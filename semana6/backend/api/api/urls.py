from django.contrib import admin
from django.urls import path, include
from api.noticias import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.noticias.urls'))
]
