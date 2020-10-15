from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Morceau, Artiste
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

def morceau_detail(request, pk):
    morceau = Morceau.objects.get(pk=pk)
    return HttpResponse(str(morceau))

class MorceauDetailView(DetailView):
    model = Morceau

class MorceauList(ListView):
    model = Morceau

class MorceauCreate(CreateView):
    model = Morceau
    fields = ['titre', 'interprete']

class MorceauDelete(DeleteView):
    model = Morceau
    success_url = reverse_lazy('musiques:morceau_list')

class MorceauUpdate(UpdateView):
    model = Morceau
    fields = ['titre','interprete']
    template_name_suffix = '_update_form'

class ArtisteDetailView(DetailView):
    model = Artiste

class ArtisteList(ListView):
    model = Artiste

class ArtisteCreate(CreateView):
    model = Artiste
    fields = ['nom']

class ArtisteDelete(DeleteView):
    model = Artiste
    success_url = reverse_lazy('musiques:artiste_list')

class ArtisteUpdate(UpdateView):
    model = Artiste
    fields = ['nom']
    template_name_suffix = '_update_form'