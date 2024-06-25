from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContactForm


def form(request):
    comment_form = CommentForm(
        {'name': 'Javi', 'url': 'https://open-bootcamp.com', 'content': 'Comentatio', 'date': '13/05/1982'})
    return render(request, 'form.html', {'comment_form': comment_form})


def goal(request):
    if request.method != 'POST':
        return HttpResponse("El metodo GET no está permitido en esta ruta", 404)

    return HttpResponse(request.POST['name'])


def widget(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():  # Fuerza la validación de clean
            # Aquí irían todas las acciones a realizar cuando los datos son correctos
            return HttpResponse("Válido")
        else:
            # Comunicamos al usuario que los datos no son válidos
            return HttpResponse("No válido")
