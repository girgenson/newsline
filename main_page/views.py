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
    """Pagination processing"""
    limit = request.GET.get('limit', 10)
    news = PieceOfNews.objects.all().order_by('-date')
    paginator = Paginator(news, limit)

    news_number = request.GET.get('page')
    news_obj = paginator.get_page(news_number)

    context = {'limit': limit, 'news_obj': news_obj}
    return render(request, 'index.html', context)


def upload(request):
    context = {}
    return render(request, 'upload_file.html', context)
