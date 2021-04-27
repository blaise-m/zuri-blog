from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/new/', PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post')
]
