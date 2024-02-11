from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    type_of_section = models.CharField(max_length=255)
    color_palette = models.CharField(max_length=255, blank=True, null=True)
    font_style = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)


class Component(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


class Parameter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    order = models.IntegerField()


class ParameterOption(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id_parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)


