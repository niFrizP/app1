from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/lista_personas.html', {'personas': personas})

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'personas/crear_persona.html', {'form': form})

def editar_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'personas/editar_persona.html', {'form': form, 'persona': persona})

def eliminar_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('lista_personas')
    return render(request, 'personas/eliminar_persona.html', {'persona': persona})
