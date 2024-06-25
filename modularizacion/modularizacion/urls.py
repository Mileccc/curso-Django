from django.contrib import admin
from django.urls import path
# importamos include para incluir la ruta de nuestra aplicacion
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # aqui incluimos la ruta urls de nuestra app
    path('comentarios/', include('comentarios.urls'))
]
