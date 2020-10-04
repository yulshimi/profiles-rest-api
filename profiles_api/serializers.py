from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(allow_blank=True, max_length=10)
