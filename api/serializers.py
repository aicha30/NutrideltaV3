from rest_framework import serializers
from nutridelta.models import Objectif, ObjectifChoice, SportChoice


class ObjectifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objectif
        fields = '__all__'

class ObjectifChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectifChoice
        fields = '__all__'

class SportChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportChoice
        fields = '__all__'
