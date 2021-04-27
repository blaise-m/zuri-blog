from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('auth/', include('blogauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('zuriblog.urls')),
]
