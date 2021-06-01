from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from desafio.planner.api.serializers.planner import PlannerSerializer
from desafio.planner.models import Planner


class PlannerView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PlannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['owner'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        queryset = Planner.objects.all().filter(owner=request.user)
        serializer = PlannerSerializer(queryset, many=True)
        return Response(serializer.data)


class PlannerViewDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Planner.objects.get(pk=pk)
        except Planner.DoesNotExist as e:
            raise Http404

    def get(self, request, pk):
        planner = self.get_object(pk)
        serializer = PlannerSerializer(planner)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        planner = self.get_object(pk)
        serializer = PlannerSerializer(planner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        planner = self.get_object(pk)
        planner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


