from django.shortcuts import render


def statics(request):
    return render(request, 'statics.html', {})
