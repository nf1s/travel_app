from rest_framework import generics

from api.serializers import FlightSerializer, ProfileSerializer, HotelSerializer
from booking.models import Profile, Hotel, Flight


# -------------------------- Profile Views ------------------------------------ #

class ProfileAPIView(generics.ListCreateAPIView):
    """
    API view provides rest endpoint to create/list companies
    """
    lookup_field = 'pk'
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ProfileRudView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view provides a rest endpoint to Retrieve/Update/Delete a profile
    """

    lookup_field = 'pk'
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# -------------------------- Hotel Views ------------------------------------ #


class HotelAPIView(generics.ListCreateAPIView):
    """
    API view provides rest endpoint to create/list Hotels
    """
    lookup_field = 'pk'
    serializer_class = HotelSerializer

    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return Hotel.objects.filter(profile=profile)

    def perform_create(self, serializer):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        serializer.save(profile=profile)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class HotelRudView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view provides a rest endpoint to Retrieve/Update/Delete a travel
    """
    lookup_field = 'pk'
    serializer_class = HotelSerializer

    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return Hotel.objects.filter(profile=profile)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# -------------------------- Flight Views ------------------------------------ #


class FlightAPIView(generics.ListCreateAPIView):
    """
    API view provides rest endpoint to create/list Flights related to a certain travel
    """
    lookup_field = 'pk'
    serializer_class = FlightSerializer

    def get_queryset(self):
        profile_id = self.request.path.split("/")[-3]
        return Flight.objects.filter(profile=profile_id)

    def perform_create(self, serializer):
        profile_id = self.request.path.split("/")[-3]
        profile = Profile.objects.get(pk=profile_id)
        serializer.save(profile=profile)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class FlightRudView(generics.RetrieveUpdateDestroyAPIView):
    """
     Flight Retrieve/Update/Delete View
     """
    lookup_field = 'pk'
    serializer_class = FlightSerializer

    def get_queryset(self):
        return Flight.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
