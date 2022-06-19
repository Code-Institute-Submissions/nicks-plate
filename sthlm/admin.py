from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Meal



@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):
    
    list_display = ('todays_meal', 'created_on')
    list_filter = ('created_on',)
    summernote_fields = ('description')

