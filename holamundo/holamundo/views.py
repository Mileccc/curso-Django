from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola Mundo!!")


def despedida(request):
    return HttpResponse("Adiooooss!!")


def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("ERES MAYOR DE EDAD!!")
    else:
        return HttpResponse("NO ERES MAYOR DE EDAD!!")
