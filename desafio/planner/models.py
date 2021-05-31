from django.db import models
from django.db.models import DO_NOTHING
from model_utils import Choices


class Planner(models.Model):

    class Meta:
        verbose_name_plural = "Listas de Tarefas"
        verbose_name = "Lista de Tarefas"

    name = models.CharField(max_length=50, verbose_name="Nome")
    owner = models.ForeignKey('auth.User', on_delete=DO_NOTHING, verbose_name="Usuario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")


class TaskPlanner(models.Model):

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    TASK_STATUS = Choices(
        ("fila", "Na Fila"),
        ("andamento", "Em andamento"),
        ("completa", "Completa"),
    )

    TASK_URGENCY = Choices(
        ("baixa", "Baixa"),
        ("media", "Média"),
        ("alta", "Alta"),
    )

    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(blank=True, verbose_name="Descricao", null=True)
    status = models.CharField(choices=TASK_STATUS, default=TASK_STATUS.fila, max_length=9, verbose_name="Status")
    urgency = models.CharField(choices=TASK_URGENCY, default=TASK_URGENCY.baixa, max_length=5, verbose_name="Urgencia")
    rgb_hex_code = models.CharField(max_length=7, verbose_name="Codigo RGB", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated = models.DateTimeField(auto_now=True, verbose_name="Atualizado em", null=True)
    planner = models.ForeignKey('Planner', on_delete=DO_NOTHING, related_name='tasks')