from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from . import models

class ArticleListView(ListView):
    model = models.Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = models.Article
    fields = ['title', 'body']
    template_name = 'article_edit.html'

class ArticleDeleteView(DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = models.Article
    fields = ['title', 'body', 'author']
    template_name = 'article_new.html'