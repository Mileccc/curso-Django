# pylint: disable=no-member
from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date, datetime


# Create your views here.

def create(request):

    rep = Reporter(first_name="Javier", last_name="Viesca",
                   email="viesca@demo.com")
    rep.save()

    art1 = Article(headline="Aprendiendo Python",
                   pub_date=date(2022, 3, 7), reporter=rep)
    art1.save()
    art2 = Article(headline="Aprendiendo Django",
                   pub_date=datetime.today(), reporter=rep)
    art2.save()
    art3 = Article(headline="Aprendiendo Java",
                   pub_date=date(2021, 12, 1), reporter=rep)
    art3.save()

    # result = art1.reporter.first_name

    # result = rep.article_set.all()

    # result = rep.article_set.filter(headline="Aprendiendo Python")

    result = rep.article_set.count()

    return HttpResponse(result)
