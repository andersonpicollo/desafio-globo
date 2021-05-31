from django.contrib import admin
from desafio.planner.models import Planner


@admin.register(Planner)
class PlannerAdmin(admin.ModelAdmin):
    pass