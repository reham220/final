"""
URL configuration for exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from . import views
from app import views

#from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('games/', views.list_games, name='list_games'),
  #    path('books/<int:book_id>/', views.book_detail, name='book_detail'),

 #   path('add-games/', views.add_books, name='add_books'),

]
