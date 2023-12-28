# clientes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Cliente
from .forms import ClienteForm

def home_clientes(request):
    return render(request, 'clientes/home.html')

@login_required
def userIndex(request):
    if request.user.is_superuser:
        return render(request, 'clientes/dashboard.html')
    elif request.user.is_staff:
        return render(request, 'clientes/dashboard.html')
    else:
        return render(request, 'clientes/dashboardLite.html')

def signup(request):
    if request.user.is_superuser:
        return render(request, 'clientes/dashboard.html')
    elif request.user.is_staff:
        return render(request, 'clientes/dashboard.html')
    else:
        return render(request, 'clientes/dashboardLite.html')
    return render(request, 'clientes/signup.html')  # Reemplaza 'clientes/signup.html' 

@login_required
def create_cliente(request):
    # Vista para agregar un nuevo cliente
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return HttpResponseRedirect(reverse('cliente_detail', args=[cliente.id]))
    else:
        form = ClienteForm()

    data = {'form': form, 'titulo_menu': 'Agregar Cliente', 'boton': 'Agregar Cliente'}
    return render(request, 'clientesAPP/create_cliente.html', data)

@login_required
def read_clientes(request):
    # Vista para desplegar el listado de clientes
    clientes = Cliente.objects.all()
    data = {'clientes': clientes}
    return render(request, 'clientesAPP/list_clientes.html', data)

@login_required
def update_cliente(request, id):
    # Vista para modificar un cliente existente
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cliente_detail', args=[cliente.id]))
    else:
        form = ClienteForm(instance=cliente)

    data = {'form': form, 'titulo': 'Modificar Cliente', 'boton': 'Aplicar cambios'}
    return render(request, 'clientesAPP/create_cliente.html', data)

@login_required
def delete_cliente(request, id):
    # Vista para eliminar un cliente
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return HttpResponseRedirect(reverse('clientes_list'))


