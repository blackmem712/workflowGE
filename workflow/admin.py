from django.contrib import admin

from workflow import models

@admin.register(models.Pessoa)
class WorkflowAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Cliente)
class WorkflowAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Funcionario)
class WorkflowAdmin(admin.ModelAdmin):
    ...