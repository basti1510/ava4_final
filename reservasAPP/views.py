# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Reserva
from .forms import ReservaForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReservaSerializer

# Vistas de la aplicación web

def home(request):
    # Página principal (landing page)
    return render(request, 'home.html')  # Asegúrate de tener el template 'home.html'

@login_required
def create_reserva(request):
    if request.method == "POST":
        form = newClientForm(request.POST, request.FILES)
        if form.is_valid():   
            instance = form.save(commit=False)
            instance.autor = request.user
            instance.save()
            form.save()
            form.cleaned_data['Nombre de cliente'] = ''
            form.cleaned_data['Telefono'] = ''
            form.cleaned_data['Email'] = ''
            form.cleaned_data['Numero de mesa'] = ''
            print("Reserva agregada correctamente")
            return HttpResponseRedirect(reverse('dashboard'))
            
    else:
        form = newClientForm()        
    data = {'form': form,
            'titulo_menu': 'Reservar pedido',
            'boton': 'Crear reserva'
            }
    return render(request, 'gestorClient/create_reserva.html', data)
    
@login_required
def read_reservas(request):
    # Vista para desplegar el listado de reservas disponibles
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'reservasAPP/list_reservas.html', context)

@login_required
def update_reserva(request, id):
    # Vista para modificar una reserva existente
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reserva_detail', args=[reserva.id]))
    else:
        form = ReservaForm(instance=reserva)

    context = {'form': form, 'titulo': 'Modificar Reserva', 'boton': 'Aplicar cambios'}
    return render(request, 'reservasAPP/create_reserva.html', context)

@login_required
def delete_reserva(request, id):
    # Vista para eliminar una reserva
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return HttpResponseRedirect(reverse('reservas_list'))


# Vistas de la API

@api_view(['GET'])
def list_reservas_api(request):
    # Vista para listar todas las reservas ordenadas por fecha
    reservas = Reserva.objects.all().order_by('fecha_reserva')
    serializer = ReservaSerializer(reservas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail_reserva_api(request, id):
    # Vista para buscar una reserva por su ID
    reserva = get_object_or_404(Reserva, id=id)
    serializer = ReservaSerializer(reserva)
    return Response(serializer.data)

@api_view(['POST'])
def create_reserva_api(request):
    # Vista para agregar una nueva reserva (POST)
    serializer = ReservaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_reserva_api(request, id):
    # Vista para modificar una reserva existente (PUT)
    reserva = get_object_or_404(Reserva, id=id)
    serializer = ReservaSerializer(instance=reserva, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_reserva_api(request, id):
    # Vista para eliminar una reserva (DELETE)
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return Response(status=204)
