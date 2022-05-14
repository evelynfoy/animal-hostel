"""animalhostel URL Configuration """
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_animals.urls'), name='home_animals_urls'),
]
