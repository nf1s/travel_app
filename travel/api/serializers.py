from rest_framework import serializers
from booking.models import Flight, Profile, Hotel

"""
    Serializers convert to correct datatypes JSON to Python dicts and Vice versa
    Ensure Validations for passed data
"""


class ProfileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = ['url', 'name']
        read_only_fields = ['url']

    def validate_name(self, value):
        request = self.context.get("request")
        company = Profile.objects.filter(user=request.user)
        if company:
            raise serializers.ValidationError("a company for this user already exists")
        return value

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class HotelSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Hotel
        fields = ['url', 'name']
        read_only_fields = ['url']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class FlightSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    product = HotelSerializer(read_only=True)

    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'date', 'stars']
        read_only_fields = ['date', 'hotel']

    def validate_stars(self, value):
        if 0 < value <= 5:
            return value
        else:
            raise serializers.ValidationError(" Number of Stars must be a number between 0 and 5")

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
