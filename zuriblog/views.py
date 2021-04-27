from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'zuriblog/index.html'
    context_object_name = 'post_list'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'zuriblog/detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'zuriblog/new_post.html'
    fields = ['title', 'author', 'body']


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'zuriblog/update_post.html'
    fields = ['title', 'body']


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'zuriblog/delete_post.html'
    success_url = reverse_lazy('index')
