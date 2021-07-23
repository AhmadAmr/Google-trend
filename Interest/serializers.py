from rest_framework import serializers
from.models import Historical
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical
        fields = ['date','term','name']
        lookup_field = 'name'
    
