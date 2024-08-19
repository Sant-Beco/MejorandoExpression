from django.shortcuts import render, get_object_or_404, redirect
from app_funcionalidad.models import Categoria
from .forms import CategoriaForm

def base(request):
    return render(request, 'categoria/base.html')

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'categoria/categoria_form.html', {'form': form})

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/categoria_list.html', {'categorias': categorias})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/categoria_form.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'categoria/categoria_confirm_delete.html', {'categoria': categoria})
