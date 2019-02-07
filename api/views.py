from django.shortcuts import render
from rest_framework import viewsets
from nutridelta.models import Objectif, ObjectifChoice, SportChoice
from .serializers import ObjectifSerializer, ObjectifChoiceSerializer, SportChoiceSerializer
from nutridelta.functions import *

class ObjectifViewSet(viewsets.ModelViewSet):
    serializer_class = ObjectifSerializer
    queryset = Objectif.objects.all()

class ObjectifChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ObjectifChoiceSerializer
    queryset = ObjectifChoice.objects.all()

class SportChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = SportChoiceSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        queryset = SportChoice.objects.all()
        if user_id:
            queryset = queryset.filter(user_id = user_id)
        return queryset

    def destroy(self, request, pk=None):
        user_id = self.request.query_params.get('user_id', None)
        SportChoice.objects.filter(pk=pk).delete()
        queryset = SportChoice.objects.all()
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset



# class ObjectifListView(ListAPIView):
#     queryset = Objectif.objects.all()
#     serializer_class = ObjectifSerializer
#
# class ObjectifDetailView(RetrieveAPIView):
#     queryset = Objectif.objects.all()
#     serializer_class = ObjectifSerializer
#
# class ObjectifRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = Objectif.objects.all()
#     serializer_class = ObjectifSerializer
