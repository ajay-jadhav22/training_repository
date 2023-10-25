"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home-page/', views.home, name='home_page'),
    path('all-books/', views.show_all_books, name='all_books'),
    path('inactive-books/', views.all_inactive_books, name='inactive_books'),
    path('active-books/', views.all_active_books, name='all_active_books'),
    path('update-book/<int:pk>/', views.update_book, name='update_book'),
    path('soft-delete/<int:pk>/', views.soft_delete, name='soft_delete'),
    path('hard-delete/<int:id>/', views.hard_delete, name='hard_delete'),
    path('restore-book/<int:pk>/', views.restore_book, name='restore_book'),
    
]
