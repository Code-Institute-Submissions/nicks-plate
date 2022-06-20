from django.shortcuts import render
from django.views.generic import ListView
from .models import Meal, Staff, Environment, Policy


class ShowMeal(ListView): 
    model = Meal
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff_list', 'environment_list', 'policy_list'] = Meal.objects.all()
        return context



