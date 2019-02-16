from rest_framework import generics

from api.serializers import FlightSerializer, HotelSerializer
from booking.models import Hotel, Flight


class HotelAPIView(generics.ListCreateAPIView):
    """
    API view provides rest endpoint to create/list Hotels
    """
    lookup_field = 'pk'
    serializer_class = HotelSerializer

    def get_queryset(self):
        return Hotel.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class HotelRudView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view provides a rest endpoint to Retrieve/Update/Delete a Hotel
    """
    lookup_field = 'pk'
    serializer_class = HotelSerializer

    def get_queryset(self):
        return Hotel.objects.filter(pk=self.kwargs["pk"])

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# -------------------------- Flight Views ------------------------------------ #


class FlightAPIView(generics.ListCreateAPIView):
    """
    API view provides rest endpoint to create/list Flights
    """
    lookup_field = 'pk'
    serializer_class = FlightSerializer

    def get_queryset(self):
        return Flight.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class FlightRudView(generics.RetrieveUpdateDestroyAPIView):
    """
     API view provides rest endpoint to Retrieve/Update/Delete a Flight
     """
    lookup_field = 'pk'
    serializer_class = FlightSerializer

    def get_queryset(self):
        return Flight.objects.filter(pk=self.kwargs["pk"])

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
