from django.urls import path
import main_page.views as views


app_name = 'main_page'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create_news', views.create_news, name = 'create_news'),
]
