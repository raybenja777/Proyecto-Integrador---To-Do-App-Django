"""
URL configuration for to_do project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from to_do_list import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='login')),  # Redirigir la ruta '/' a 'login'
    path('admin/', admin.site.urls), # Ruta para el panel de administración
    path('login/', auth_views.LoginView.as_view(), name='login'), # Ruta para iniciar sesión
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # Ruta para cerrar sesión
    path('registro/', views.RegistroView.as_view(), name='registro'), # Ruta para registrar usuario
    path('to_do_list/', include('to_do_list.urls')), # Ruta para la lista de tareas
    path('accounts/profile/', RedirectView.as_view(url='/task/list/', permanent=False)),  # Redirigir el perfil a la lista de tareas
    
]
