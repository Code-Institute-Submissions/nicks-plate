from django.shortcuts import render
from django.views import generic
from .models import Meal


class ShowMeal(generic.ListView):
    
    model = Meal
    template_name = 'index.html'

