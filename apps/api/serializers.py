from rest_framework.serializers import ModelSerializer
from dictionary.models import HanziSet

class HanziSetSerializer(ModelSerializer):
    class Meta:
        model = HanziSet
        fields = ('id', )
