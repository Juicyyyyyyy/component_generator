from django.contrib import admin
from .models import Project, Component, Parameter, ParameterOption

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'owner_id', 'description', 'type_of_section', 'color_palette', 'font_style', 'language')
    list_filter = ('type_of_section', 'color_palette', 'font_style', 'language')
    search_fields = ('description', 'owner_id__username')  # to search by owner's username

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'project_id')
    list_filter = ('project_id',)
    search_fields = ('project_id__description',)

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    search_fields = ('name',)

@admin.register(ParameterOption)
class ParameterOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_parameter', 'value')
    list_filter = ('id_parameter',)
    search_fields = ('name', 'id_parameter__name')
