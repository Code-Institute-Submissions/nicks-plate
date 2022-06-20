from django.shortcuts import render
from django.views.generic import ListView
from .models import Meal, Staff, Environment, Policy


class IndexView(ListView): 
    """  """
    model = Meal
    template_name = 'index.html'

    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['staff_list'] = Staff.objects.all()
        context['environment_list'] = Environment.objects.all()
        context['policy_list'] = Policy.objects.all()
        return context
