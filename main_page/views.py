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
    limit = request.GET.get('limit', 10)
    news = PieceOfNews.objects.all().order_by('-date')
    paginator = Paginator(news, limit)
    all = list(PieceOfNews.objects.all())

    news_number = request.GET.get('page')
    news_obj = paginator.get_page(news_number)


    context = {'news': news, 'paginator': paginator, 'all': all,
               'limit': limit, 'news_obj': news_obj}
    return render(request, 'index.html', context)


def index2(request):
    # Read the limit query
    limit = request.GET.get('limit', 10)

    news = PieceOfNews.objects.all().order_by('-date')

    # Use the limit in the paginator
    paginator = Paginator(news, limit)
    all = list(PieceOfNews.objects.all())
    news_on_page = 3
    context = {'news': news, 'paginator': paginator, 'all': all,
               'news_on_page': news_on_page}

    class Meta:
        verbose_name_plural = 'piece of news'

    return render(request, 'index.html', context)
