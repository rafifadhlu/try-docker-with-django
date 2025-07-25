from django.urls import path
from .views import ArticleIndexView,ArticleAddView

from django.contrib.auth.decorators import login_required



app_name = 'article'
urlpatterns = [
    path('', login_required(ArticleIndexView), name='index'),
    path('add/', login_required(ArticleAddView), name='add'),
]