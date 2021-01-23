from django.shortcuts import render, redirect
from . models import PieceOfNews
from django.core.paginator import Paginator
from . forms import PieceOfNewsForm


def create_news(request):
    form = PieceOfNewsForm(request.POST or None)
    if request.method != 'POST':
        form = PieceOfNewsForm()
    else:
        form = PieceOfNewsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page:index')

    context = {'form': form}
    return render(request, 'create_news.html', context)




def index(request):
    limit = 10
    limit = request.GET.get('limit', 10)
    news = PieceOfNews.objects.all().order_by('-date')
    paginator = Paginator(news, limit)
    all = list(PieceOfNews.objects.all())
    context = {'news': news, 'paginator': paginator, 'all': all, 'limit': limit}

    class Meta:
        verbose_name_plural = 'piece of news'

    return render(request, 'index.html', context)

