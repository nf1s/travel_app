import graphene
from graphene_django.types import DjangoObjectType

from booking.models import Hotel, Flight


class HotelType(DjangoObjectType):
    class Meta:
        model = Hotel


class FlightType(DjangoObjectType):
    class Meta:
        model = Flight


class Query(graphene.ObjectType):
    all_hotels = graphene.List(HotelType)
    all_flights = graphene.List(FlightType)

    hotel = graphene.Field(
        HotelType,
        id=graphene.Int(),
        name=graphene.String()
    )

    flight = graphene.Field(
        FlightType,
        id=graphene.Int(),
        origin=graphene.String(),
        destination=graphene.String()
    )

    def resolve_all_hotels(self, info, **kwargs):
        return Hotel.objects.all()

    def resolve_all_flights(self, info, **kwargs):
        return Flight.objects.all()

    def resolve_hotel(self, info, **kwargs):
        pk = kwargs.get('id')
        name = kwargs.get('name')

        if pk is not None:
            return Hotel.objects.get(pk=pk)

        if name is not None:
            return Hotel.objects.get(name=name)

        return None

    def resolve_flight(self, info, **kwargs):
        pk = kwargs.get('id')
        origin = kwargs.get('origin')
        destination = kwargs.get('destination')

        if pk is not None:
            return Flight.objects.get(pk=pk)

        if origin is not None:
            return Flight.objects.get(origin=origin)

        if destination is not None:
            return Flight.objects.get(destination=destination)

        return None


schema = graphene.Schema(query=Query)
