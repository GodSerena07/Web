
from django.contrib import admin
from django.urls import path
from Estates import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
]