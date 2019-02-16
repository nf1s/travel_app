from rest_framework import serializers

from booking.models import Flight, Hotel

"""
    Serializers convert to correct datatypes JSON to Python dicts and Vice versa
    Ensure Validations for passed data
"""


class HotelSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Hotel
        fields = ['url', 'name', 'address', 'stars']
        read_only_fields = ['url']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class FlightSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Flight
        fields = ['url', 'origin', 'destination', 'date']
        read_only_fields = ['date']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
