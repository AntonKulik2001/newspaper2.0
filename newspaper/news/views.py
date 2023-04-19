from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from datetime import datetime

class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'mainnews.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class Textnews(DetailView):
    model = Post
    template_name = 'textnews.html'
    context_object_name = 'post'
