# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm


def lista_libros(request):
    libros = Libro.objects.all()

    busqueda = request.GET.get('buscar')

    if busqueda:
        libros = libros.filter(titulo__icontains=busqueda)

    return render(request, 'libros/lista_libros.html', {
        'libros': libros
    })


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()

    return render(request, 'libros/formulario_libro.html', {
        'form': form,
        'titulo': 'Registrar libro'
    })


def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)

        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'libros/formulario_libro.html', {
        'form': form,
        'titulo': 'Editar libro'
    })


def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    libro.estado = 'BAJA'
    libro.save()

    return redirect('lista_libros')