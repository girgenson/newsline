from django.urls import path
import main_page.views as views


app_name = 'mainpage'
urlpatterns = [
    path('', views.index, name = 'index'),
]