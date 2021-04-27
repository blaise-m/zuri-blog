from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('new-post/', PostCreateView.as_view(), name='new-post'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update-post/', PostUpdateView.as_view(), name='update-post'),
    path('<int:pk>/delete-post/', PostDeleteView.as_view(), name='delete-post')
]
