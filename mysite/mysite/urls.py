from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),  # Цей шлях важливий для доступу до адміністративної панелі
    # Ваші інші шляхи
]
