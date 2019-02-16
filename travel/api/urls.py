from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from api.views import FlightAPIView
from api.views import FlightRudView
from api.views import HotelAPIView
from api.views import HotelRudView

schema_view = get_swagger_view(title='Booking API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^hotel/(?P<pk>\d+)/$', HotelRudView.as_view(), name='hotel-rud'),
    url(r'^flight/(?P<pk>\d+)/$', FlightRudView.as_view(), name='flight-rud'),

    url(r'^hotel/$', HotelAPIView.as_view(), name='hotel-create'),
    url(r'^flight/$', FlightAPIView.as_view(), name='flight-create'),
]
