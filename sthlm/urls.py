from . import views
from django.urls import path


urlpatterns = [
    path('', views.ShowMeal.as_view()),
    path('', views.ShowStaff.as_view()),
    path('', views.ShowEnvironment.as_view()),
    path('', views.ShowPolicy.as_view()),
]