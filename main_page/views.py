from django.shortcuts import render
from . models import PieceOfNews


def index(request):
    news = PieceOfNews.objects.all().order_by('-date')
    context = {'news': news}
    return render(request, 'index.html', context)

    class Meta:
        verbose_name_plural = 'piece of news'
