from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('app_blog.urls')),
]
# app_blog/urls.py
from django.urls import path
from app_blog import views

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]
