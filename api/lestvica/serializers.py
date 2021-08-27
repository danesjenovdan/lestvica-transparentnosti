from rest_framework import serializers

from lestvica.models import Municipality


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = [
            'id',
            'name',
            'email',
            'rank',
            'budget',
            'population',
            'total_score',
            'total_bucket',
            'groups',
            'questions',
            'recommendations',
            'bucket_peers',
        ]


class SmallMunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = [
            'id',
            'name',
            'rank',
            'total_score',
            'total_bucket',
            'groups',
        ]
