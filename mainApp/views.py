from django.shortcuts import render
from django.views import View
from .models import *


# def home(request):
#     return render(request,'home.html')

class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class Blog(View):
    def get(self, request):
        years = []
        articles = Article.objects.all()
        for article in articles:
            years.append(str(article.date)[:4])
            years=set(years)
        context = {
                'years': years,
                'articles': articles,
            }
        return render(request, 'blog.html', context)


class Maqola(View):
    def get(self, request):
        return render(request, 'maqola.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')
