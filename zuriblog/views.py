from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Post, Comment


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
    fields = ['title', 'body']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'zuriblog/update_post.html'
    fields = ['title', 'body']


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'zuriblog/delete_post.html'
    success_url = reverse_lazy('index')


class CommentCreateView(generic.CreateView):
    model = Comment
    template_name = 'zuriblog/add_comment.html'
    fields = ['body']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        post_id = self.kwargs['pk']
        post = Post.objects.get(pk=post_id)
        self.object.post = post
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
