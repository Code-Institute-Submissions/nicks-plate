from . import views
from django.urls import path


urlpatterns = [
    path('', views.ShowMeal.as_view(), name='home')
]