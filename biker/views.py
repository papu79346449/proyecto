from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Evento
from .forms import EventoForm
def Form_event(request):
    eventos = Evento.objects.order_by('nombre_evento')    
    return render(request, 'biker/Form_event.html', {'eventos':eventos})

def evento_detail(request, pk):
        evento = get_object_or_404(Evento, pk=pk)
        return render(request, 'biker/evento_detail.html', {'evento': evento})

def evento_new(request):
        form = EventoForm()
        return render(request, 'biker/evento_edit.html', {'form': form})
# Create your views here.
