import graphene
from graphene_django.types import DjangoObjectType
from booking.models import Profile, Hotel, Flight


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class HotelType(DjangoObjectType):
    class Meta:
        model = Hotel


class FlightType(DjangoObjectType):
    class Meta:
        model = Flight


class Query(graphene.ObjectType):
    all_profiles = graphene.List(ProfileType)
    all_hotels = graphene.List(HotelType)
    all_flights = graphene.List(FlightType)

    profile = graphene.Field(ProfileType, id=graphene.Int(), name=graphene.String())
    hotel = graphene.Field(HotelType, id=graphene.Int(), name=graphene.String())
    flight = graphene.Field(FlightType, id=graphene.Int(), origin=graphene.String(), destination=graphene.String())


    def resolve_all_profiles(self, info, **kwargs):
        return Profile.objects.all()

    def resolve_all_hotels(self, info, **kwargs):
        return Hotel.objects.select_related('profile').all()

    def resolve_all_flights(self, info, **kwargs):
        return Flight.objects.select_related('profile').all()

    def resolve_profile(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Profile.objects.get(pk=id)

        if name is not None:
            return Profile.objects.get(name=name)

        return None

    def resolve_hotel(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Hotel.objects.get(pk=id)

        if name is not None:
            return Hotel.objects.get(name=name)

        return None


    def resolve_flight(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Flight.objects.get(pk=id)

        return None

schema = graphene.Schema(query=Query)
