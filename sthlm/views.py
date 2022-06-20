from django.shortcuts import render
from django.views.generic import ListView
from .models import Meal, Staff, Environment, Policy


class ShowMeal(ListView): 
    model = Meal
    template_name = 'index.html'


class ShowStaff(ListView):   
    model = Staff
    template_name = 'index.html'


class ShowEnvironment(ListView):  
    model = Environment
    template_name = 'index.html'


class ShowPolicy(ListView):   
    model = Policy
    template_name = 'index.html'