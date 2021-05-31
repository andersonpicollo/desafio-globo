from desafio.planner.models import Planner
from rest_framework import serializers


class PlannerSerializer(serializers.ModelSerializer):

    created = serializers.DateTimeField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Planner
        fields = ('id', 'name', 'created')

    def create(self, validated_data):
        planner = super(PlannerSerializer, self).create(validated_data)
        planner.save()
        return planner
