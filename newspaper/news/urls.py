from django.urls import path
from .views import NewsList, Textnews

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', Textnews.as_view())
]