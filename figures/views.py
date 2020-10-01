from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from django.urls import reverse_lazy
from figures.models import Dictionary, Figures
from django.template import loader


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class DictionaryCreateView(CreateView):
    fields = ('name', 'description', 'url')
    model = Dictionary
    template_name = 'figures/r_add_form.html'


class DictionaryUpdateView(UpdateView):
    fields = ('name', 'description', 'url')
    model = Dictionary
    template_name = 'figures/r_add_form.html'


class DictionaryDeleteView(DeleteView):
    model = Dictionary
    success_url = reverse_lazy('figures:tables')
    template_name = 'figures/r_delete.html'


class FiguresCreateView(CreateView):
    fields = ('name', 'description', 'url')
    model = Figures
    template_name = 'figures/r_add_form.html'


class FiguresUpdateView(UpdateView):
    fields = ('name', 'description', 'url')
    model = Figures
    template_name = 'figures/r_add_form.html'


class FiguresDeleteView(DeleteView):
    model = Figures
    success_url = reverse_lazy('figures:tables')
    template_name = 'figures/r_delete.html'


def TablesView(request):
    dictionary_table = Dictionary.objects.all()
    figures_table = Figures.objects.all()
    template = loader.get_template('figures/r_list.html')
    context = {
        'dictionary_table':dictionary_table,
        'figures_table':figures_table,
    }
    return HttpResponse(template.render(context,request))
