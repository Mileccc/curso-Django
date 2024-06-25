# pylint: disable=no-member
import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

# Create your views here.


def update(request):
    author = Author.objects.get(id=1)
    author.name = "Javier"
    author.email = "javierin@hotmail.com"
    author.save()
    return HttpResponse("Update correctly")


def queries(request):

    # Obtener todos los elementos
    authors = Author.objects.all()

    # Obtener autores según filtro
    filtered = Author.objects.filter(email="bryanleach@example.net")

    # Obtener un único objeto(filtrado)
    author = Author.objects.get(id=1)

    # Limitar resultados de una consulta. (10 primeros)
    limits = Author.objects.all()[:10]

    # Saltando los elementos que queramos (10 elementos saltando los 5 primeros)
    offsets = Author.objects.all()[5:15]

    # METODOS DE ORDENACION
    orders = Author.objects.all().order_by('email')

    # Obtener todos los elementos cuyo id sea menor o igual a 15
    filtered2 = Author.objects.filter(id__lte=15)
    # __lte --> Menor o igual a
    # __gte --> Mayor o igual a
    # __lt --> Menor que
    # __gt --> Mayor que
    # __contains --> Contiene
    # __startswith --> Comienza por
    # __endswith --> Termina por
    # __iexact --> Igual a
    # __icontains --> Contiene (ignora mayúsculas y minúsculas)
    # __in --> En la lista
    # __isnull --> Nulo
    # __year__month__day --> Fecha, mes, año
    # __range --> Rango
    # __year__month__day__hour__minute__second --> Fecha, mes, año, hora, minuto, segundo
    # __year__month__day__hour__minute__second__microsecond --> Milisegundo
    # __year__month__day__hour__minute__second__microsecond__tzinfo --> Zona horaria
    # Obtener todos los autores que contienen en su nombre la palabra 'music'
    filtered3 = Author.objects.filter(name__contains="music")

    # CONTEXTO
    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets, 'orders': orders, 'filtered2': filtered2, 'filtered3': filtered3})
