from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.


def test(request):
    return HttpResponse("Funciona correctamente.")


def create(request):
    # En 2 pasos.
    # comment = Comment(name="Javi", score=5, comment="Este es un comentario")
    # comment.save()

    # De forma directa
    comment = Comment.objects.create(name="Pedro")
    return HttpResponse("Ruta para probar la creación de modelos.")


def delete(request):
    # Primero tenemos que buscar el objeto.
    # comment = Comment.objects.get(id=1)

    # Con comment.delete() borramos dicha fila.
    # comment.delete()

    # de forma directa. Usando filtros (.filter().delete())
    Comment.objects.filter(id=1).delete()
    return HttpResponse("Ruta para probar el borrado de modelos")
