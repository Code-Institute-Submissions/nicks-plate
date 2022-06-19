from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Meal, Environment, Staff, Policy



@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):
    
    list_display = ('todays_meal', 'created_on')
    list_filter = ('created_on',)
    summernote_fields = ('description')


@admin.register(Environment)
class EnvironmentAdmin(SummernoteModelAdmin):

    list_display = ('environment_title', 'created_on')
    list_filter = ('created_on',)
    summernote_fields = ('description')


@admin.register(Staff)
class StaffAdmin(SummernoteModelAdmin):

    list_display = ('staff_title', 'created_on')
    list_filter = ('created_on',)
    summernote_fields = ('description')


@admin.register(Policy)
class PolicyAdmin(SummernoteModelAdmin):

    list_display = ('policy_title', 'created_on')
    list_filter = ('created_on',)
    summernote_fields = ('description')
