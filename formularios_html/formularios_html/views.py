from django.shortcuts import render
from django.http import HttpResponse

# GET


def getform(request):
    return render(request, 'form.html', {})


def getgoal(request):
    if request.method != 'GET':
        return HttpResponse("El metodo POST no está soportado para esta ruta")

    name = request.GET['name']
    return render(request, 'success.html', {'name': name})

# POST


def postform(request):
    return render(request, 'postform.html', {})


def postgoal(request):
    if request.method != 'POST':
        return HttpResponse("El metodo GET no está soportado para esta ruta")

    info = request.POST['info']
    return render(request, 'postsuccess.html', {'info': info})
