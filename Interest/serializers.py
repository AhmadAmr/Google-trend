from rest_framework import serializers
from.models import Historical ,Region
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical
        fields = ['date','term','name']
        lookup_field = 'name'
    
class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        lookup_field = id