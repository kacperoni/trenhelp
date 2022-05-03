from ast import Delete
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,ListView, DetailView, CreateView,
                                DeleteView,UpdateView)
from trenhelp.models import Training,Exercise
from django import forms

class TrenhelpHomeView(TemplateView):
    template_name= 'trenhelp/home.html'

class TrenhelpListView(ListView):
    model = Training
    ordering = ['-date_created']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TrenhelpDetailView(DetailView):
    model = Training
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TrenhelpCreateView(CreateView):
    model = Training
    fields = ['name','date_created']

class TrenhelpDeleteView(DeleteView):
    model = Training
    success_url = reverse_lazy('list_view')

class TrenhelpUpdateView(UpdateView):
    model = Training
    fields = ['name']
    template_name_suffix = '_update_form'

class TrenhelpExerciseUpdateView(UpdateView):
    model = Exercise
    fields = ['name','sets','reps','weight']
    template_name_suffix='_update_form'

class TrenhelpExerciseCreateView(CreateView):
    model = Exercise
    fields = ['training','name','sets','reps','weight']

class TrenhelpExerciseDeleteView(DeleteView):
    model = Exercise
    success_url = reverse_lazy('trenhelp:trenhelp_detail')