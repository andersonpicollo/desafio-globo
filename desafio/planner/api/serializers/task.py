from desafio.planner.models import TaskPlanner
from rest_framework import serializers


class TaskPlannerSerializer(serializers.ModelSerializer):

    created = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = TaskPlanner
        fields = ('id', 'name', 'description', 'status',
                  'created', 'urgency', 'rgb_hex_code', 'planner')

    def create(self, validated_data):
        task = super(TaskPlannerSerializer, self).create(validated_data)
        task.save()
        return task
