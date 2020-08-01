from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView)
from .models import Post
from .forms import PostCreateForm


class PostsLstView(ListView):
    """Вывод десяти последних опубликованных постов от свежих к старым"""
    model = Post
    template_name = 'blog/index.html'
    queryset = Post.objects.order_by('-published_date')[:10]


class PostCreateView(CreateView):
    """Создание нового поста. После создания пользователь будет перенаправлен на страницу созданного поста."""
    model = Post
    template_name = 'blog/new_post.html'
    form_class = PostCreateForm


class PostDetailView(DetailView):
    """Вывод поста. Страница, на которой можно прочитать полный текст статьи"""
    model = Post
    template_name = 'blog/post.html'
