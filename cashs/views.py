from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from . import models 

class CashListView(ListView):
    model = models.Cash
    context_object_name = "cashs"

