"""
URL configuration for EVA4_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from reservasAPP.views import home, create_reserva, read_reservas, update_reserva, delete_reserva
from reservasAPP.views import list_reservas_api, detail_reserva_api, create_reserva_api, update_reserva_api, delete_reserva_api
from clientes.views import signup, create_cliente, read_clientes, update_cliente, delete_cliente, userIndex





urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', userIndex, name="dashboard"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('reservas/', read_reservas, name='reserva_list'),
    path('reservas/crear/', create_reserva, name='reserva_create'),
    path('reservas/editar/<int:id>/', update_reserva, name='reserva_update'),
    path('reservas/eliminar/<int:id>/', delete_reserva, name='reserva_delete'),
    path('api/reservas/', list_reservas_api, name='list_reservas_api'),
    path('api/reservas/<int:id>/', detail_reserva_api, name='detail_reserva_api'),
    path('api/reservas/crear/', create_reserva_api, name='create_reserva_api'),
    path('api/reservas/editar/<int:id>/', update_reserva_api, name='update_reserva_api'),
    path('api/reservas/eliminar/<int:id>/', delete_reserva_api, name='delete_reserva_api'),
    path('clientes/registro/', create_cliente, name='registro_cliente'),
    path('clientes/', read_clientes, name='clientes_list'),
    path('clientes/editar/<int:id>/', update_cliente, name='cliente_update'),
    path('clientes/eliminar/<int:id>/', delete_cliente, name='cliente_delete'),
]
